import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

#create db 
db=client['dbStudent']

#crate collection
cln=db['collStudent']

#inserting/creating one document in collection
#d1={"name":"Akash Sane","degree":"BCA","course":"MCA","dur_years":2,"Semesters":4}
#cln.insert_one(d1)
#print("One Document inserted successfully!!")
#d2={"name":"Sagar Sharma","degree":"BBA","course":"MBA","dur_years":2,"Semesters":4}
#cln.insert_one(d2)
#print("Document inserted successfully!!")

#moreData=[{"name":"Vikas Patil","course":"MCA","dur_years":2,"Semesters":4},
#      {"name":"Umesh Date","course":"MPM","dur_years":2,"Semesters":4},
#      {"name":"Walmik Pande","course":"MBA","dur_years":2,"Semesters":4}]

#cln.insert_many(moreData)
#print("All Documents inserted successfully!!")


fone=collection.find_one({'name':'xyz'})
print(fone)
