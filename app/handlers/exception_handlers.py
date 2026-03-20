from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.base import AppException


async def app_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    app_exc = exc if isinstance(exc, AppException) else AppException()
    return JSONResponse(
        status_code=app_exc.status_code,
        content={"detail": app_exc.detail},
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppException, app_exception_handler)
