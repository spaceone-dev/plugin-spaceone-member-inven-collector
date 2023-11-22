from typing import Generator
from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer
from .manager.member_manager import MemberManager

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return {"metadata": {"options_schema": {}}}


@app.route("Collector.collect")
def collector_collect(params: dict) -> Generator[dict, None, None]:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")

    member_mgr = MemberManager()
    return member_mgr.collect_resources(options, secret_data, schema)
