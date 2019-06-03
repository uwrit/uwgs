import requests
from .types import Payload, get_headers
from typing import List


class Membership:
    def __init__(self, session, url):
        self._session = session
        self._url = url

    def members(self, group_id: str, query: dict, header: dict) -> object:
        self._url += '/group/{}/member'.format(group_id)
        return Payload(self._session.get(self._url, params=query, headers=header))

    def count(self, group_id: str, query: dict, header: dict) -> object:
        self._url += '/group/{}/member'.format(group_id)
        return Payload(self._session.get(self._url, params=query, headers=header))

    def find_member(self, group_id: str, member_id: str, query: dict, header: dict) -> object:
        self._url += '/group/{}/member/{}'.format(group_id, member_id)
        return Payload(self._session.get(self._url, params=query, headers=header))

    def effective_members(self, group_id: str, header: dict) -> object:
        self._url += '/group/{}/effective_member'.format(group_id)
        return Payload(self._session.get(self._url, headers=header))

    def effective_count(self, group_id: str, query: dict, header: dict) -> object:
        self._url += '/group/{}/effective_member'.format(group_id)
        return Payload(self._session.get(self._url, params=query, headers=header))

    def find_effective_member(self, group_id: str, member_id: str, query: dict, header: dict) -> object:
        self._url += '/group/{}/effective_member/{}'.format(
            group_id, member_id)
        return Payload(self._session.get(self._url, params=query, headers=header))
