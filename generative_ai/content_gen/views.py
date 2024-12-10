from typing import Any

from fastapi import APIRouter  # type: ignore
from pydantic import ValidationError

from content_gen.exceptions import InvalidContentGenRequestException
from content_gen.models import ContentGenRequest, ContentGenResponse
from content_gen.operations import content_gen_api


router = APIRouter(prefix="/articles")


@router.post("/api/content-gen/get-completion")
def get_completion(payload: dict[str, Any]) -> ContentGenResponse:
    try:
        request = ContentGenRequest(**payload)
        completion: ContentGenResponse = content_gen_api.get_completion(request)

    except (TypeError, ValidationError) as e:
        raise InvalidContentGenRequestException(f"Message: {e}")

    return completion