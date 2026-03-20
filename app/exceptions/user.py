from app.exceptions.base import AppException


class UserNotFoundError(AppException):
    status_code = 404
    detail = "User not found"


class UserValidationError(AppException):
    status_code = 400
    detail = "Invalid user data"


class UserAlreadyExistsError(AppException):
    status_code = 400
    detail = "Email already registered"

