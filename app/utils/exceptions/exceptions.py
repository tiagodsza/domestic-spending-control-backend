from starlette.status import HTTP_404_NOT_FOUND


class HTTPException(Exception):
    status_code: int
    message: str


class NotFoundException(HTTPException):
    def __init__(self, message: str = 'Não encontrado'):
        self.message = message
        self.status_code = HTTP_404_NOT_FOUND