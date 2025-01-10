import logging
from colorama import Fore
import repository.mongo as mongo

db = mongo.connect()
log = logging.getLogger(__name__)

def login(username, password):
    log.info("Retrieved user data from the database for login.")
    return db.users.find_one({"$and":[{"name": username}, {"password": password}]})

def register(username, password, admin):
    log.info("Added a new user into the database.")
    db.users.insert_one({"name": username, "admin": admin, "password": password})
    print(Fore.GREEN,"Registration successful!" + Fore.RESET,"")

def get_parts(type):
    log.info("Retrieved part data from database for shopping.")
    return db.parts.find({"type": type})

def get_model(model):
    log.info("Retrieved model information from database.")
    return db.parts.find_one({"model": model})

def get_all_order_history():
    log.info("Retrieved order history from database.")
    return db.orders.find()

def get_order_history(name):
    log.info("Retrieved user order history from database.")
    return db.orders.find({"user": name})

def add_order(cart, name, price):
    specs = []
    for part in cart:
        specs.append(part['model'])
    log.info("Added user's order to database.")
    db.orders.insert_one({"user": name, "specs": ', '.join(specs), "price": price})

def change_price(model, new_price):
    log.info("Updated price of a model in the database.")
    db.parts.update_one({"model": model}, {"$set":{"price": new_price}})

def get_users():
    log.info("Retrieved list of users from the database.")
    return db.users.find()

def delete_user(name):
    log.info("Deleted a user from the database.")
    return db.users.find_one_and_delete({"name": name})

def delete_orders(user):
    log.info("Deleted user's orders from the database.")
    db.orders.delete_many({"user": user})