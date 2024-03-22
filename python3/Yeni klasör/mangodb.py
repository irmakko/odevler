import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://irmakkoc:7fGkHjIOqDJKiWXE@cluster0.z4sbgl0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client["database"]
collection=db["logfile"]
with open("mongo_parse.txt", "r")as file:
    for line in file:
        log_entry={"log_message":line.strip()}
        collection.insert_one(log_entry)
print("LogFile dosyası Mongodb'ye kaydedildi:)")


