#Kayden Linner
#04/11/2021
#Module 5.3

from pymongo import MongoClient

#MongoDB Application Connection String
url = "mongodb+srv://admin:admin@cluster0.isvtw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connects to cluster in MongoDB
client = MongoClient(url)

#connects to pytech database
db = client.pytech

#students collection
students = db.students

#locate all students
student_list = students.find({})

print("\n -- QUERY ALL STUDENTS --")

for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\nFirst Name: " + doc["first_name"] + "\nLast Name: " + doc["last_name"] + "\n")

#find document by student_id
kayden = students.find_one({"student_id": "1007"})

#output
print("\n -- QUERY SINGLE STUDENT --")
print("\nStudent ID: " + kayden["student_id"] + "\nFirst Name: " + kayden["first_name"] + "\nLast Name: " + kayden["last_name"] + "\n")

#end of program
input("\nEnd of program, press a button to quit...")