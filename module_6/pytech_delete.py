#Kayden Linner
#04/17/2021
#Module 6.3

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

print(" \n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

#loop through students and print
for doc in student_list:
    print("  Student ID " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

paul = {
    "student_id": "1010",
    "first_name": "Paul",
    "last_name": "Walker",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": "2.3",
            "start_date": "03/15/2021",
            "end_date": "05/16/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Chris Soriano",
                    "grade": "D"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java Design",
                    "instructor": "Darrel Payne",
                    "grade": "D-"
                }
            ]
        }
    ]
}

print("\n -- INSERT STATEMENTS -- ")
paul_student_id = students.insert_one(paul).inserted_id

print("  Inserted student record into the students collection with document_id " + str(paul_student_id))

#find_one() method
student_paul = students.find_one({"student_id": "1010"})

#display inserted doc
print("\n  -- DISPLAYING STUDENT PAUL WALKER --")
print("  Student ID: " + student_paul["student_id"] + "\n  First Name: " + student_paul["first_name"] + "\n  Last Name: " + student_paul["last_name"] + "\n")

print("\n  -- DELETE STATEMENT -- ")
print(" Student ID " + student_paul["student_id"] + " has been deleted.")
delete_paul_doc = students.delete_one({"student_id": "1010"})

updated_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in updated_student_list:
    print("  Student_ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

input("\nEnd of program, press a button to quit...")