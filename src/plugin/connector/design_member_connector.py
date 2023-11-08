import logging
from spaceone.core.error import ERROR_REQUIRED_PARAMETER
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


class DesignMemberConnector(BaseConnector):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        self._check_secret_data(secret_data)

    @staticmethod
    def list_members(department_name) -> dict:

        # Using mock dataset
        response = {
            'department_name': department_name,
            'members': [
                {
                    'id': 'member-01', 'name': 'soonja', 'part': 'designer', 'state': 'solo',
                    'email': 'soonja@spaceone.com', 'join_date': '2020-08-01'
                },
                {
                    'id': 'member-02', 'name': 'sangchul', 'part': 'designer', 'state': 'married',
                    'email': 'sangchul@spaceone.com', 'join_date': '2012-09-01'
                }
            ]
        }

        return response

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if 'user_email' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.user_email')

        if 'api_key' not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key='secret_data.api_key')
