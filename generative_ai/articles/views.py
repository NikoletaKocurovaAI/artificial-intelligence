from fastapi import APIRouter  # type: ignore


router = APIRouter(prefix="/articles")


@router.get("/hello")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, World!"}
