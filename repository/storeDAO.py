import repository.mongo as mongo

db = mongo.connect()

def login(username, password):
    user = (db.users.find_one({"name": username}))
    print(user)