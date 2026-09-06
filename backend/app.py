import uvicorn
from litestar import Litestar,Request
from services import ApplicationService
from exception_handlers import handle_unexpected_exception
from litestar_mcp import LitestarMCP,MCPConfig


def on_startup(app):
    print('starting up....')

    from config import db_connection
    app.state.db_connection = db_connection
    app.state.application_service = ApplicationService(db_connection=db_connection)

def on_shutdown(app):
    print("shutting down....")
    db_engine = getattr(app.state,"db_engine", None)
    if db_engine is not None:
        db_engine.disponse()

def provide_api_service(request:Request)-> ApplicationService:
    return request.app.state.application_service

def create_app() -> Litestar:

    from litestar.di import Provide
    from api import APIController
    from management import LoadGraphDatabasePlugin

    return Litestar(
        plugins=[LoadGraphDatabasePlugin(), LitestarMCP(MCPConfig(include_in_schema=True, auth=None))],
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
        exception_handlers={Exception: handle_unexpected_exception},
        dependencies={'service': Provide(provide_api_service)},
        route_handlers=[APIController]

    )

if __name__ == '__main__':
    import unicorn
    uvicorn.run("app:main", host="127.0.0.1", port=8000,factory=True,reload=True)