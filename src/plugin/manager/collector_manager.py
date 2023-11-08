import logging
from typing import Generator

from spaceone.core.error import *
from spaceone.core.manager import BaseManager

_LOGGER = logging.getLogger('__name__')


class CollectorManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.cloud_service_group = None
        self.cloud_service_type = None
        self.region_name = None
        self.provider = None

    def verify_client(self, options: dict, secret_data: dict, schema: str) -> None:
        raise NotImplementedError('Method not implemented!')

    def collect(self, options: dict, secret_data: dict, schema: str) -> Generator[dict, None, None]:
        raise NotImplementedError('Method not implemented!')

    @staticmethod
    def make_response(resource_data: dict, match_keys: list,
                      resource_type: str = 'inventory.CloudService') -> dict:
        return {
            'state': 'SUCCESS',
            'resource_type': resource_type,
            'match_keys': match_keys,
            'resource_data': resource_data
        }

    def error_response(self, error: Exception, resource_type: str = 'inventory.CloudService') -> dict:
        if not isinstance(error, ERROR_BASE):
            error = ERROR_UNKNOWN(message=error)

        _LOGGER.error(f'[error_response] ({self.region_name}) {error.error_code}: {error.message}', exc_info=True)
        return {
            'state': 'FAILURE',
            'error_message': error.message,
            'resource_type': 'inventory',
            'resource_data': {
                'provider': self.provider,
                'cloud_service_group': self.cloud_service_group,
                'cloud_service_type': self.cloud_service_type,
                'resource_type': resource_type
            }
        }
