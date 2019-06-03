from .group import Group
from .membership import Membership
from .search import Search
import requests
from typing import List
from .types import get_headers


class Client:
    def __init__(self, client_cert: str, client_key: str, url: str):
        session = requests.Session()
        session.cert = (client_cert, client_key)
        session.verify = True

        self._session = session
        self._url = url

    def get_group(self, group_id: str, if_none_match: str = None):
        header = get_headers(**{'If-None-Match': if_none_match})
        group = Group(self._session, self._url)
        return group.get(group_id, header)

    def get_members(self, group_id: str):
        query = {'source=registry': 'registry'}
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.members(group_id, query, header)

    def get_membership_count(self, group_id: str):
        query = {
            'view': 'count',
            'source=registry': 'registry'
        }
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.count(group_id, query, header)

    def find_member(self, group_id: str, member_id: str):
        query = {
            'source=registry': 'registry'
        }
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.find_member(group_id, member_id, query, header)

    def get_effective_members(self, group_id: str):
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.effective_members(group_id, header)

    def get_effective_membership_count(self, group_id: str):
        query = {
            'view': 'count',
            'source=registry': 'registry'
        }
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.effective_count(group_id, query, header)

    def find_effective_member(self, group_id: str, member_id: str):
        query = {
            'source=registry': 'registry'
        }
        header = get_headers()
        membership = Membership(self._session, self._url)
        return membership.find_effective_member(group_id, member_id, query, header)

    def search(self,
            name: str = None,
            stem: str = None,
            scope: str = None,
            member: str = None,
            ty: str = None,
            owner: str = None,
            affiliate: str = None,
            instructor: str = None):
        query = {
            "name": name,
            "stem": stem,
            "scope": scope,
            "member": member,
            "type": ty,
            "owner": owner,
            "affiliate": affiliate,
            "instructor": instructor,
            "source=registry": 'registry'
        }
        header = get_headers()
        search = Search(self._session, self._url)
        return search.get(query, header)
