"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

from typing import List

from pydantic import BaseModel

class University(BaseModel):
    """University model.
    """
    web_page: str
    name: str



class UnsavedUniversity(BaseModel):
    """Full University model.
    """
    web_pages: List[str]
    name: str
    alpha_two_code: str
    state_province: str
    domains: List[str]
    country: str
