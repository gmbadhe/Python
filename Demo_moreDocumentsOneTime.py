import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

#create db 
db=client['dbStudent']

#crate collection
cln=db['collStudent']

#inserting/creating multiple document in collection
moreData=[{"name":"Vikas Patil","course":"MCA","dur_years":2,"Semesters":4},
       {"name":"Umesh Date","course":"MPM","dur_years":2,"Semesters":4},
       {"name":"Walmik Pande","course":"MBA","dur_years":2,"Semesters":4}]

cln.insert_many(moreData)
print("All Documents inserted successfully!!")

