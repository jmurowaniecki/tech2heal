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
        os.environ["MONGO_PROTOCOL"],
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOSTNAME"],
        os.environ["MONGO_DATABASE"],
        ))
    return client[os.environ["MONGO_DATABASE"]]
