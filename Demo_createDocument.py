import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

#create db 
db=client['dbStudent']

#crate collection
cln=db['collStudent']

#inserting/creating one document in collection
d1={"name":"xyz","degree":"BCA","course":"MCA","dur_years":2,"Semesters":4}
cln.insert_one(d1)

print("One Document inserted successfully!!")

