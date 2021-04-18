#Kayden Linner
#04/17/2021
#Module 6.2

from pymongo import MongoClient

#MongoDB Application Connection String
url = "mongodb+srv://admin:admin@cluster0.isvtw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connects to cluster in MongoDB
client = MongoClient(url)

#connects to pytech database
db = client.pytech

#student collection
students = db.students

#find all students
student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#all students are looped through
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#update 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Linner-Geist"}})

#redisplay document with student_id of 1007
kayden = students.find_one({"student_id": "1007"})

#print statement for styling
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

#print statement of updated student_id 1007 document
print("  Student ID: " + kayden["student_id"] + "\n  First Name: " + kayden["first_name"] + "\n  Last Name: " + kayden["last_name"] + "\n")

#program finished
input("\nEnd of program, press a button to quit...")