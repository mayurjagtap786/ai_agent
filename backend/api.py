from litestar import Controller, get
from litestar.params import FromQuery
from services import ApplicationService
from dto import Node

class APIController(Controller):

    path="/api"

    @get('components', mcp_tool='list_components')
    def list_components(self,service:ApplicationService, names: FromQuery[list[str]] | None = None, extract_children : FromQuery[bool]= False) -> list[Node]:
        return service.list_components(components=names, extract_children=extract_children)