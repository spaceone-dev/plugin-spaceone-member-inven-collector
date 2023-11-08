import logging

from spaceone.core.manager import BaseManager
from ..connector.design_member_connector import DesignMemberConnector


class DataSourceManager(BaseManager):

    @staticmethod
    def init_response(options: dict) -> dict:
        return {
            'metadata': {
                'supported_resource_type': [
                    'cloud_service',
                    'cloud_service_type'
                ],
                'supported_schedules': [
                    'hours'
                ],
                'supported_features': [
                    'garbage_collection'
                ],
                'filter_format': [],
                'options_schema': {
                    'required': ['regions'],
                    'order': ['regions'],
                    'type': 'object',
                    'properties': {
                        'regions': {
                            'title': 'Region Filter',
                            'type': 'array',
                            'items': {
                                'enum': [
                                    'ap-northeast-1',
                                    'ap-northeast-2'
                                ]
                            }
                        }
                    }
                }
            }
        }

    @staticmethod
    def verify_plugin(options: dict, secret_data: dict, schema: str = None) -> None:
        design_member_connector = DesignMemberConnector()
        design_member_connector.verify_client(options, secret_data, schema)
