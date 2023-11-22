import logging
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger("cloudforet")


class MemberConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def list_members() -> dict:
        return {
            'members_info': [
                {
                    'id': 'member-01', 'name': 'soonja', 'part': 'designer', 'state': 'solo',
                    'email': 'soonja@spaceone.com', 'join_date': '2020-08-01'
                },
                {
                    'id': 'member-02', 'name': 'sangchul', 'part': 'developer', 'state': 'married',
                    'email': 'sangchul@spaceone.com', 'join_date': '2012-09-01'
                }
            ]
        }
