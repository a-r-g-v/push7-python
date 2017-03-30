from typing import List, Dict, Any, Union
from push7.push import Push, PushWithQuery
from push7.exceptions import (UnauthorizedException, ForbiddenException,
                              NotFoundException, MethodNotAllowedException,
                              ClientErrorException, ServerErrorException)


def __throw_exception(status_code, error):
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

    def push(self, title, body, icon_url, url, transmission_time):
        # type: (str, str, str, str, Union[datetime, None]) -> Push
        return Push(title, body, icon_url, url, self, transmission_time)

    def push_with_query(self, title, body, icon_url, url, transmission_time,
                        mode, parameters):
        # type: (str, str, str, str, Union[datetime, None], PushWithQuery.Mode, List[str]) -> PushWithQuery
        return PushWithQuery(title, body, icon_url, url, transmission_time,
                             self, mode, parameters)

    def _do_api_request(self, path, jsonify_dict):
        # type: (str, Dict[str, Any]) -> Any
        import requests
        response = requests.post(path, json=jsonify_dict)
        body = response.json()

        if 'error' in body:
            __throw_exception(response.status_code, body['error'])  # pylint: disable=W0212

        return body
