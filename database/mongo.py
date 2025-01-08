from pymongo import MongoClient
import json

def main():
    client = MongoClient("mongodb://localhost:27017/")

    db = client.get_database("test")

