import pydantic
from abc import ABC
from typing import Optional,Type


class AbstrackUser(pydantic.BaseModel,ABC):
    name: str
    password: str

    @pydantic.field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if 2 < len(value) < 10:
            raise ValueError("Length of password must be greater than 2 or equal to 8")
        return value

    @pydantic.validator("name")
    @classmethod
    def name_length(cls, value: str) -> str:
        if 3 < len(value) < 50:
            raise ValueError("Length of name must be greater than 2 or equal to 50")
        return value

class CreateUser(AbstrackUser):
    name: str
    password: str

class UpdateUser(AbstrackUser):
    name: Optional[str] = None
    password: Optional[str] = None

SCHEMA_CLASS = Type[CreateUser | UpdateUser]
SHEMA = CreateUser | UpdateUser
