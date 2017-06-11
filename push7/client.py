from typing import List, Dict, Any, Union
from datetime import datetime
from push7.push import Push, PushWithQuery
from push7.exceptions import (UnauthorizedException, ForbiddenException,
                              NotFoundException, MethodNotAllowedException,
                              ClientErrorException, ServerErrorException)
from requests import Session


def make_requests_with_retries():
    # type: () -> Session
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry
    session = Session()
    retries = Retry(
        total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    session.mount('http://', HTTPAdapter(max_retries=retries))
    return session


def _throw_exception(status_code, error):
    # type: (int, str) -> None

    if status_code == 401:
        raise UnauthorizedException(error)

    elif status_code == 403:
        raise ForbiddenException(error)

    elif status_code == 404:
        raise NotFoundException(error)

    elif status_code == 405:
        raise MethodNotAllowedException(error)

    elif status_code / 100 == 4:
        raise ClientErrorException(error)

    elif status_code / 100 == 5:
        raise ServerErrorException(error)

    raise Exception(error)


class Client(object):
    def __init__(self, appno, apikey, endpoint="https://api.push7.jp/api/v1"):
        # type: (str, str, str) -> None
        self.__appno = appno
        self.__apikey = apikey
        self.__endpoint = endpoint

    @property
    def appno(self):
        # type: () -> str
        return self.__appno

    @property
    def endpoint(self):
        # type: () -> str
        return self.__endpoint

    def make_headers(self):
        # type: () -> Dict[str, str]
        return {'Authorization': 'Bearer {token}'.format(token=self.__apikey)}

    def push(self, title, body, icon_url, url, transmission_time=None):
        # type: (str, str, str, str, Union[datetime, None]) -> Push
        return Push(
            title,
            body,
            icon_url,
            url,
            transmission_time=transmission_time,
            client=self)

    def push_with_query(self,
                        title,
                        body,
                        icon_url,
                        url,
                        mode,
                        parameters,
                        transmission_time=None):
        # type: (str, str, str, str, PushWithQuery.Mode, List[str], Union[datetime, None]) -> PushWithQuery
        return PushWithQuery(
            title,
            body,
            icon_url,
            url,
            mode,
            parameters,
            transmission_time=transmission_time,
            client=self)

    def _do_api_request(self, path, jsonify_dict, headers=None):
        # type: (str, Dict[str, Any], Union[Dict[str, Any], None]) -> Any

        if headers is None:
            headers = {}

        headers.update(self.make_headers())

        requests = make_requests_with_retries()
        response = requests.post(
            self.endpoint + path, json=jsonify_dict, headers=headers)
        body = response.json()

        if 'error' in body:
            _throw_exception(response.status_code, body['error'])  # pylint: disable=W0212

        return body
