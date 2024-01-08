from typing import Union
from datetime import datetime

from fastapi import APIRouter, Body
from black import FileMode, format_str


from server.schemas import (
    FlattenCodeRequestSchema,
    FlattenCodeResponseSchema,
    ErrorResponseSchema,
)

router = APIRouter()


@router.get("/")
async def home() -> dict:
    return {
        "message": "Welcome to Python Command Flattener API",
        "version": "1.0",
        "documentation_url": "/docs",
        "status": "Running",
        "server_time": datetime.today().strftime("%Y-%m-%d %H:%M%S"),
    }


@router.post("/flatten_code")
async def flatten_code(
    flatten_code_request_body: FlattenCodeRequestSchema = Body(...),
) -> Union[FlattenCodeResponseSchema, ErrorResponseSchema]:
    try:
        return {
            "flattened_code_string": format_str(
                flatten_code_request_body.code_string,
                mode=FileMode(
                    line_length=10_000,
                    magic_trailing_comma=False,
                ),
            ).replace("\n", "")
        }
    except Exception as e:
        return {"error": str(e)}
