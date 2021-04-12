#Kayden Linner
#04/11/2021
#Module 5.2


from pymongo import MongoClient

#MongoDB Application Connection String
url = "mongodb+srv://admin:admin@cluster0.isvtw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

#connects to cluster in MongoDB
client = MongoClient(url)

#connects to pytech database
db = client.pytech

#prints out what collections are in the connection
print("\n-- PyTech Collection List --")
print(db.list_collection_names())

#exit message
input("\nEnd of program, press a button to quit...")