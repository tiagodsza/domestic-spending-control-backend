from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND


class NotFoundException(HTTPException):
    def __init__(self, message: str = 'Not Found.'):
        self.detail = message
        self.status_code = 404

class InvalidValueException(HTTPException):
    def __init__(self, name):
        self.detail = f'Invalid {name}'
        self.status_code = 422