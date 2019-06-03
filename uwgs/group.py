import requests
from .types import Payload, get_headers


class Group:
    def __init__(self, session, url):
        self._session = session
        self._url = url

    def get(self, group_id: str, header: dict) -> Payload:
        self._url += '/group/{}'.format(group_id)
        return Payload(self._session.get(self._url, headers=header))
