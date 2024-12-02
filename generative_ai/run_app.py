from fastapi import FastAPI  # type: ignore

from articles.views import router as articles_router  # type: ignore
from weather.views import router as weather_router  # type: ignore
from content_gen.views import router as content_gen_router  # type: ignore


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(articles_router, prefix="/v1", tags=["articles"])
    app.include_router(weather_router, prefix="/v1", tags=["weather"])
    app.include_router(content_gen_router, prefix="/v1", tags=["content_gen"])

    return app


app: FastAPI = create_app()
