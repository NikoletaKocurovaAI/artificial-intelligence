from fastapi import FastAPI  # type: ignore

from articles.views import router as articles_router  # type: ignore


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(articles_router, prefix="/v1")

    return app


app: FastAPI = create_app()
