from fastapi import FastAPI, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from reusable_mongodb_connection import get_db
import httpx
from json import loads

from .settings import Settings, get_settings
from .__version__ import __version__

app = FastAPI(version=__version__, openapi_tags=[{"name": "root"}])


async def check_service(url: str) -> bool:
    async with httpx.AsyncClient() as client:
        return (await client.get(url)).is_success


@app.get("/test", tags=["root"])
async def test(settings: Settings = Depends(get_settings)):
    return {
        "name": settings.app_name,
        "can connect to microservice `places`": await check_service(
            "http://places:1234/openapi.json"
        ),
        "can connect to microservice `facts`": await check_service(
            "http://facts:1234/openapi.json"
        ),
    }


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    root_openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
        tags=app.openapi_tags,
    )

    places_openapi_schema = loads(httpx.get("http://places:1234/openapi.json").text)
    places_openapi_schema = loads(httpx.get(f"http://{settings.place_url}/place").text)
    facts_openapi_schema = loads(httpx.get("http://facts:1234/openapi.json").text)

    for dict_key in {"paths", "components"}:
        root_openapi_schema[dict_key] = (
            root_openapi_schema.get(dict_key, {})
            | places_openapi_schema.get(dict_key, {})
            | facts_openapi_schema.get(dict_key, {})
        )

    for list_key in {"tags"}:
        root_openapi_schema[dict_key] = (
            root_openapi_schema.get(list_key, [])
            + places_openapi_schema.get(list_key, [])
            + facts_openapi_schema.get(list_key, [])
        )

    # openapi_schema["info"]["x-logo"] = {
    #     "url": ""
    # }

    app.openapi_schema = root_openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
