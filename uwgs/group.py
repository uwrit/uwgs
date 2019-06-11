import requests
from .types import Payload, get_headers
import attr


class Group:
    def __init__(self, session, url):
        self._session = session
        self._url = url

    def get(self, group_id: str, header: dict) -> Payload:
        self._url += '/group/{}'.format(group_id)
        return Payload(self._session.get(self._url, headers=header))

@attr.s
class GroupResponseMeta:
    resource_type: str = attr.ib(default='group')
    version: str = attr.ib(default='')
    reg_id: str = attr.ib(default='')
    id: str = attr.ib(default='')
    self_ref = attr.ib(default='')
    member_ref: str = attr.ib(default='')
    timestamp: int = attr.ib(default=0)

@attr.s
class Group:
    reg_id: str = attr.ib(default='')
    
