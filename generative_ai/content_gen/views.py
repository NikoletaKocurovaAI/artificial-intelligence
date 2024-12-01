from typing import Any

from fastapi import APIRouter  # type: ignore
from pydantic import ValidationError

from content_gen.exceptions import InvalidContentGenRequestException
from content_gen.models import ContentGenRequest
from content_gen.operations import ContentGenApi


router = APIRouter(prefix="/articles")


@router.post("/api/content-gen/get-completion")
def get_completion(payload: dict[str, Any]) -> dict[str, Any]:
    try:
        request = ContentGenRequest(**payload)
    except (TypeError, ValidationError) as e:
        raise InvalidContentGenRequestException(f"Message: {e}")
