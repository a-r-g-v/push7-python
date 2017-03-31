# coding: utf8
import enum
from typing import List, Dict, Any, Union
from datetime import datetime
import simplejson as json


class Push(object):
    def __init__(self,
                 title,
                 body,
                 icon_url,
                 url,
                 transmission_time=None,
                 client=None):
        # type: (str, str, str, str, Union[datetime, None], Any) -> None
        self.title = title
        self.body = body
        self.icon_url = icon_url
        self.url = url
        self.client = client
        self.transmission_time = datetime.now(
        ) if transmission_time is None else transmission_time

    def to_dict(self):
        # type: () -> Dict[str, Any]
        return {
            'title': self.title,
            'body': self.body,
            'icon': self.icon_url,
            'url': self.url,
            'transmission_time':
            self.transmission_time.strftime('%Y-%m-%d %H:%m'),
        }

    @property
    def path(self):
        # type: () -> str
        appno = self.client.appno
        return "/{appno}/send".format(appno=appno)

    def send(self):
        # type: () -> None
        self.client._do_api_request(self.path, self.to_dict())  # pylint: disable=W0212


class PushWithQuery(Push):
    class Mode(enum.Enum):
        _or = "OR"
        _and = "AND"
        _nor = "NOR"
        _nand = "NAND"

    def __init__(self,
                 title,
                 body,
                 icon_url,
                 url,
                 mode,
                 parameters,
                 transmission_time=None,
                 client=None):
        # type: (str, str, str, str, PushWithQuery.Mode, List[str], Union[datetime, None], Any) -> None
        super(PushWithQuery, self).__init__(title, body, icon_url, url,
                                            transmission_time, client)
        self.mode = mode
        self.parameters = parameters

    def to_dict(self):
        # type: () -> Dict[str, Any]
        push_dict = super(PushWithQuery, self).to_dict()
        push_dict.update({
            'query': {
                'mode': self.mode.value,
                'params': self.parameters
            }
        })
        return push_dict
