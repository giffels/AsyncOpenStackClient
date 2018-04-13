from .client import Client


class NovaClient(Client):
    def __init__(self, session=None, api_url=None):
        super().__init__('nova', ['flavors', 'servers'], session, api_url)

    async def init_api(self):
        await super().init_api()
        self.api.servers.actions["force_delete"] = {"method": "DELETE", "url": "servers/{}"}
        self.api.servers.actions["get"] = {"method": "GET", "url": "servers/{}"}
        self.api.servers.actions["list"] = {"method": "GET", "url": "servers/detail"}
        self.api.servers.add_action("force_delete")
        self.api.servers.add_action("get")
        self.api.flavors.actions["list"] = {"method": "GET", "url": "flavors/detail"}
