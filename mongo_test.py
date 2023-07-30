import pymongo

client= pymongo.MongoClient("mongodb+srv://subhramondal:subhra100@cluster0.yeaw9sz.mongodb.net/?retryWrites=true&w=majority")

db=client.test
print(db)

d = {
    "name" : "subhra",
    "address" : "kolkata"
}

d = {
    "name" : "subhra",
    "address" : "kolkata"
}


db2=client["mongo_test"]
coll=db2["test"]
coll.insert_one(d)








