# -*- coding: utf-8 -*-

"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

import os

from typing import List

from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles


from models.HTTPError import HTTPError
from models.University import University, UnsavedUniversity
from models.AllowedTypes import AllowedTypes

from config.database import connect_db

def custom_openapi():
    """Setup custom OpenAPI body and description.
    """
    if app.openapi_schema:
        return app.openapi_schema

    with open("README.md", "r", encoding='UTF-8') as file:
        readme_contents = file.read().splitlines(True)
    file.close()

    app.openapi_schema = get_openapi(
        title="FastAPI Testing",
        version="0.1.0",
        description="\n".join(readme_contents[1:]),
        routes=app.routes,
    )

    return app.openapi_schema


MDB = connect_db()
app = FastAPI()
app.openapi = custom_openapi
app.mount("/.assets", StaticFiles(directory=".assets"), name="assets")

@app.get("/", tags=[""])
def get_server_information():
    """Main/index page.

    Returns:
        object: JSON data with environment info.
    """

    data = []

    for name in MDB.list_collection_names():
        data.append(name)

    return {
        "environment": os.environ["APP_ENV"],
        "collections": data
    }


@app.get(
    "/{kind}/{value}",
    tags=["University"],
    responses={
        200: { "model": List[University] },
        400: {
            "model": HTTPError,
            "description": "This endpoint always raises an error",
            }
        })
def list_universities(kind: AllowedTypes, value: str, name: Optional[str] = None):
    """Search for universities on given country filtering by name fragment (optional).

Args:
- **kind** (str): Can be `alpha_two_code` or `country`.

- **value** (str): Use `BR` or `Brazil`.

- **name** (optional): Use it on query string. Defaults to None.

Returns:
- JSON: `{ "web_page": "university.web_pages.com", "name": "University Name" }`
    """

    if kind not in ["alpha_two_code", "country"]:
        raise HTTPException(status_code=400, detail="Invalid kind… See documentation.")

    query, data = {}, []
    query[kind] = value

    if name:
        query["name"] = { "$regex": ".*%s.*" % name }

    for university in MDB.university.find(query):
        data.append({
            "web_page": university["web_pages"][0],
            "name"    : university["name"]
        })

    return data


@app.post("/university", response_model=University, tags=["University"])
async def update_item(
    university: UnsavedUniversity,
):
    """Save a new University entry.

Args:
- **university** (UnsavedUniversity): University object.

Returns:
- JSON: `{ "web_page": "university.web_pages.com", "name": "University Name" }`
    """
    MDB.university.insert_one({
        "web_pages": university.web_pages,
        "name": university.name,
        "alpha_two_code": university.alpha_two_code,
        "state-province": university.state_province,
        "domains": university.domains,
        "country": university.country,
    })
    university = MDB.university.find_one({
        "name": university.name
    })

    return JSONResponse(status_code=201, content={
        "web_page": university["web_pages"][0],
        "name"    : university["name"]
    })
