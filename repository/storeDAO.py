from colorama import Fore
import repository.mongo as mongo

db = mongo.connect()

def login(username, password):
    return db.users.find_one({"$and":[{"name": username}, {"password":password}]})

def register(username, password, admin):
    print(Fore.GREEN,"Registration successful!" + Fore.RESET,"")
    #TODO make this actually save and persist the created user

def get_parts(type):
    return db.parts.find({"type": type})