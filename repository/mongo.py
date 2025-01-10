import logging
from pymongo import MongoClient

log = logging.getLogger(__name__)

def connect():
    try:
        client = MongoClient("mongodb://localhost:27017/")
    except ConnectionError: 
        print("Error: unable to connect to MongoDB database.")
    else:
        db = client.get_database("computershop")
        log.info("Connection to MongoDB database established.")
        return db