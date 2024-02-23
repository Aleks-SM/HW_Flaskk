from error import HttpError
from pydantic import ValidationError
from schema import SCHEMA_CLASS

def validate_json(schema: SCHEMA_CLASS, json_data: dict | list):
    try:
        return schema(**json_data).dict(exclude_unset=True)
    except ValidationError as err:
        error = err.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)