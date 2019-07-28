import pymongo
print("welcome to mongodb")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["users"]

mydict = { "name": "John", "age": 23,"dob":"01-06-1996" }

#x = mycol.insert_one(mydict)
query ={ "name":"John"}
y = mycol.find_one(query)

print(y)

z = mycol.update_one(query,{"$set":{"flag":"true"}})
xy = mycol.find_one(query)

print(xy)

yz = mycol.delete_one(query)
zx = mycol.find_one(query)

print(zx)
