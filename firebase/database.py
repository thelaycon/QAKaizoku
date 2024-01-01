import os

from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Avoid storing credentials in accessible files
cred = credentials.Certificate("qakaizoku-firebase.json")
firebase_admin.initialize_app(cred, {"databaseURL":DATABASE_URL})

class Database:
    def __init__(self):
        pass
        
        
    def saveJobsToFirebase(self, data):
        ref = db.reference("/jobs")
        ref.update(data)
    
    def getJobsFromFirebase(self, limit: int) -> dict:
        ref = db.reference("/jobs")
        # Fetch jobs by limit
        if limit is None:
            data = ref.get()
        else:
            data = ref.order_by_child("timestamp").limit_to_first(limit).get()        
        return data
        
 