from colorama import Fore
import repository.mongo as mongo

db = mongo.connect()

def login(username, password):
    return db.users.find_one({"$and":[{"name": username}, {"password": password}]})

def register(username, password, admin):
    db.users.insert_one({"name": username, "admin": admin, "password": password})
    print(Fore.GREEN,"Registration successful!" + Fore.RESET,"")

def get_parts(type):
    return db.parts.find({"type": type})

def get_model(model):
    return db.parts.find_one({"model": model})

def get_all_order_history():
    return db.orders.find()

def get_order_history(name):
    return db.orders.find({"user": name})

def add_order(cart, name, price):
    specs = []
    for part in cart:
        specs.append(part['model'])
    db.orders.insert_one({"user": name, "specs": ', '.join(specs), "price": price})

def change_price(model, new_price):
    db.parts.update_one({"model": model}, {"$set":{"price": new_price}})

def get_users():
    return db.users.find()

def delete_user(name):
    return db.users.find_one_and_delete({"name": name})

def delete_orders(user):
    db.orders.delete_many({"user": user})