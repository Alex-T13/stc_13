from dynaconf import settings
from fastapi import FastAPI
from fastapi import status

from api import db
from api import schemas
from framework.logging_for_humans import configure_logging

API_URL = "/api/v1"

app = FastAPI(
    description="example of API based on FastAPI and SqlAlchemy frameworks",
    docs_url=f"{API_URL}/docs/",
    openapi_url=f"{API_URL}/openapi.json",
    redoc_url=f"{API_URL}/redoc/",
    title="Z37 API",
    version="1.0.0",
)

logger = configure_logging("api")


@app.post(f"{API_URL}/blog/post/", status_code=status.HTTP_201_CREATED)
async def new_post(payload: schemas.PostApiSchema) -> schemas.PostApiSchema:
    logger.debug("creating new post")

    new_post = payload.data
    logger.debug(f"payload: {payload}")

    obj = db.create_post(new_post)
    logger.debug(f"created obj: {obj}")

    (obj, nr_likes) = db.get_single_post(obj.id)
    logger.debug(f"read obj: {obj}, nr_likes: {nr_likes}")

    post = schemas.PostSchema(
        id=obj.id,
        author_id=obj.author_id,
        content=obj.content,
        nr_likes=str(nr_likes),
    )
    logger.debug(f"built post: {post}")

    response = schemas.PostApiSchema(data=post)
    logger.debug(f"built response: {response}")

    return response