from pymongo import MongoClient
import certifi
client=MongoClient("mongodb+srv://admin:Piyush321@cluster0.qkml9gv.mongodb.net/?appName=Cluster0",
                   tlsCAFile=certifi.where())

db=client["menu_db"]
menu_collection=db["menu"]
