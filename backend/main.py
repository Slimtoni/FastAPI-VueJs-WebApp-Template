import uvicorn

from app import config
from app.utils.app_exceptions import AppExceptionCase
from fastapi import FastAPI

from app.routers import foo
from app.config.database import engine

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
)
from app.utils.app_exceptions import app_exception_handler

from fastapi.middleware.cors import CORSMiddleware

config.database.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8082"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


@app.exception_handler(AppExceptionCase)
async def custom_app_exception_handler(request, e):
    return await app_exception_handler(request, e)


app.include_router(foo.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
