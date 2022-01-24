# -*- coding: utf-8 -*-

"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

import os

from typing import List

from typing import Optional
from fastapi import FastAPI, HTTPException

from models.HTTPError import HTTPError
from models.University import University
from models.AllowedTypes import AllowedTypes

from lib.database import connect_db

app = FastAPI()
MDB = connect_db()

@app.get("/")
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

- **value** (str): Use `br` or `Brazil`.

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
