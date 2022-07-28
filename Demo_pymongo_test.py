import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['pyproject']

collection=db['myStudent']

#inserting one document in collection

d1={"name":"Akash Sane","course":"MCA","dur_years":2,"Semesters":4}
collection.insert_one(d1)

d2={"name":"Sagar Sharma","course":"MBA","dur_years":2,"Semesters":4}
collection.insert_one(d2)

#inserting multiple documents at a time in collection

mulData=[{"name":"Vikas Patil","course":"MCA","dur_years":2,"Semesters":4},
         {"name":"Umesh Date","course":"MBA","dur_years":2,"Semesters":4},
         {"name":"Walmik Pande","course":"MCA","dur_years":2,"Semesters":4}]

collection.insert_many(mulData)

#finding one document from collection

fone=collection.find_one({'name':'Akash Sane'})
print(fone)
