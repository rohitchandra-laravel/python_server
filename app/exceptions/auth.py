from app.exceptions.base import AppException


class AuthError(AppException):
    status_code = 401
    detail = "Authentication failed"

