from typing import Optional

from pydantic import BaseModel


class FlattenCodeRequestSchema(BaseModel):
    code_string: Optional[str]

    class Config:
        schema_extra = {
            "example": {"code_string": "Python code in the form of a string."}
        }


class FlattenCodeResponseSchema(BaseModel):
    flattened_code_string: str


class ErrorResponseSchema(BaseModel):
    error: str
