from .types import Payload, get_headers
import requests


class Search:
    def __init__(self, session, url):
        self._session = session
        self._url = url

    def get(self, query: dict, header: dict = get_headers()) -> object:
        self._url += '/search'
        return Payload(self._session.get(self._url, params=query, headers=header))
