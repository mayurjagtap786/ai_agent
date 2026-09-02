from litestar import Controller, get


class APIController(Controller):

    path='/api'
    @get('components', mcp_tool='list_components')
    def get_components(self):
        pass