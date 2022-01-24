"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

from enum import Enum

class AllowedTypes(str, Enum):
    """Allowed types model.
    """
    ALPHA_TWO_CODE = "alpha_two_code"
    COUNTRY = "country"
