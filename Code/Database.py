from pymongo import MongoClient
import urllib.parse
import environ

env = environ.Env()
environ.Env.read_env()
class Database:
    def get_database():
        PASSWORD=env("PASSWORD_IS")
        CONNECTION_STRING="mongodb+srv://VSNSAINIVAS:"+PASSWORD+"@cluster0.ciz9ysq.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(CONNECTION_STRING)
        return client['invertedindex']['update']
    
    def Database(email, update):
        Success = "Success"
        try:
            db = Database.get_database()
            upadateIs = {"email":email, "update":update}
            db.insert_one(upadateIs)
        except Exception as e:
            print(e)
            Success = "Failure"
        return [Success]
        