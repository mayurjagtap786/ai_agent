import logging

from litestar import  Request
from litestar.response import Response

logger = logging.getLogger(__name__)
def handle_unexpected_exception(request: Request, exec: Exception) -> Response:
    logger.exception("Unhandled exception error", exec_info=exec)

    return Response(
        content={'detail','Internal server error'},
        status_code=500,
        media_type="appliation/json",
    )
