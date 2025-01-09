import repository.mongo as mongo
import entities.user as userent
import entities.order as orderent
import entities.part as partent

db = mongo.connect()

def login(username, password):
    doc = (db.users.find_one({"$and":[{"name": username}, {"password":password}]}))
    if(doc == None): print("oops")
    else: 
        print(doc['name'] + doc['password'] + str(doc['admin']))
        return userent.User(doc['name'], doc['password'], doc['admin'])