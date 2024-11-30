from fastapi import FastAPI

from articles.views import router as articles_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(articles_router, prefix="/v1")

    return app


app: FastAPI = create_app()
