from colorama import Fore
import repository.mongo as mongo

db = mongo.connect()

def login(username, password):
    return db.users.find_one({"$and":[{"name": username}, {"password":password}]})

def register(username, password, admin):
    print("added!")