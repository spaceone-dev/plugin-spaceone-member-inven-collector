from typing import Generator

from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer
from .manager.data_source_manager import DataSourceManager
from .manager.design_member_manager import DesignMemberManager

app = CollectorPluginServer()


@app.route('Collector.init')
def collector_init(params: dict) -> dict:
    """ init plugin by options

    Args:
        params (CollectorInitRequest): {
            'options': 'dict',    # Required
            'domain_id': 'str'
        }

    Returns:
        PluginResponse: {
            'metadata': 'dict'
        }
    """

    options = params['options']
    data_source_mgr = DataSourceManager()
    return data_source_mgr.init_response(options)


@app.route('Collector.verify')
def collector_verify(params: dict) -> None:
    """ Verifying collector plugin

    Args:
        params (CollectorVerifyRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'schema': 'str',
            'domain_id': 'str'
        }

    Returns:
        None
    """
    options = params['options']
    secret_data = params['secret_data']
    schema = params.get('schema')

    data_source_mgr = DataSourceManager()
    data_source_mgr.verify_plugin(options, secret_data, schema)


@app.route('Collector.collect')
def collector_collect(params: dict) -> Generator[dict, None, None]:
    """ Collect external data

    Args:
        params (CollectorCollectRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'schema': 'str',
            'domain_id': 'str'
        }

    Returns:
        Generator[ResourceResponse, None, None]
        {
            'state': 'SUCCESS | FAILURE',
            'resource_type': 'inventory.CloudService | inventory.CloudServiceType | inventory.Region',
            'resource_data': 'dict',
            'match_keys': 'list',
            'error_message': 'str'
            'metadata': 'dict'
        }
    """

    options = params['options']
    secret_data = params['secret_data']
    schema = params.get('schema')

    design_member_mgr = DesignMemberManager()
    return design_member_mgr.collect(options, secret_data, schema)


@app.route('Job.get_tasks')
def job_get_tasks(params: dict) -> dict:
    """ Get job tasks

    Args:
        params (JobGetTaskRequest): {
            'options': 'dict',      # Required
            'secret_data': 'dict',  # Required
            'domain_id': 'str'
        }

    Returns:
        TasksResponse: {
            'tasks': 'list'
        }

    """
    pass
