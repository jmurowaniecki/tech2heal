"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

from pydantic import BaseModel

class HTTPError(BaseModel):
    """Basic HTTP error handler.
    """
    detail: str

    class Config:
        """Throwable object configuration.
        """
        schema_extra = {
            "example": {"detail": "HTTPException raised."},
        }
