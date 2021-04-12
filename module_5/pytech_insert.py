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

#Kayden's information to be inserted
kayden = {
    "student_id": "1007",
    "first_name": "Kayden",
    "last_name": "Linner",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": "3.65",
            "start_date": "03/15/2021",
            "end_date": "05/16/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Chris Soriano",
                    "grade": "A"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java Design",
                    "instructor": "Darrel Payne",
                    "grade": "A"
                }
            ]
        }
    ]
}

#Pace's information to be inserted
pace = {
    "student_id": "1008",
    "first_name": "Pace",
    "last_name": "Kral",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": "2.53",
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
                    "grade": "C"
                }
            ]
        }
    ]
}

#Shane's information to be inserted
shane = {
    "student_id": "1009",
    "first_name": "Shane",
    "last_name": "O'Neill",
    "enrollments": [
        {
            "term": "Term 2",
            "gpa": "3.23",
            "start_date": "03/15/2021",
            "end_date": "05/16/2021",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Chris Soriano",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java Design",
                    "instructor": "Darrel Payne",
                    "grade": "C-"
                }
            ]
        }
    ]
}

#students collection
students = db.students

#insert statements & output
print("\n -- INSERT STATEMENTS --")
kayden_student_id = students.insert_one(kayden).inserted_id
print("  Inserted student record Kayden Linner into the students collection with student_id " + str(kayden_student_id))

pace_student_id = students.insert_one(pace).inserted_id
print("  Inserted student record Pace Kral into the students collection with student_id " + str(pace_student_id))

shane_student_id = students.insert_one(shane).inserted_id
print("  Inserted student record Shane O'Neill into the students collection with student_id " + str(shane_student_id))

#End of program
input("\nEnd of program, press a button to quit...")