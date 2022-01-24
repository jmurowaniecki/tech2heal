"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

from pydantic import BaseModel

class University(BaseModel):
    """University model.
    """
    web_page: str
    name: str
