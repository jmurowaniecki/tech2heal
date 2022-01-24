"""FastAPI testing for Tech2Heal

@Author John Murowaniecki <john@compilou.com.br>

See README.md and Makefile for usage and more information.
"""

import os
import pymongo

def connect_db():
    """Get database driver.

    Returns:
        object: MongoDB object.
    """
    client = pymongo.MongoClient("%s://%s:%s@%s/%s?retryWrites=true&w=majority" % (
        os.environ["APP_PROTOCOL"],
        os.environ["APP_USERNAME"],
        os.environ["APP_PASSWORD"],
        os.environ["APP_HOSTNAME"],
        os.environ["APP_DATABASE"],
        ))
    return client[os.environ["APP_DATABASE"]]
