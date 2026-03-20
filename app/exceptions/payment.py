from app.exceptions.base import AppException


class PaymentError(AppException):
    status_code = 400
    detail = "Payment failed"

