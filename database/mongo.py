from pymongo import MongoClient

def connect():
    try:
        client = MongoClient("mongodb://localhost:27017/")
    except ConnectionError: 
        print("Error: unable to connect to MongoDB database.")
    else:
        db = client.get_database("computershop")
        return db