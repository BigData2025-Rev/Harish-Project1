from colorama import Fore
import repository.mongo as mongo
import entities.user as userent
import entities.order as orderent
import entities.part as partent

db = mongo.connect()

def login(username, password):
    return db.users.find_one({"$and":[{"name": username}, {"password":password}]})