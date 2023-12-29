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
        ref.push(data)
    
    def remove_job(self, data):
        pass
        
    def update_job(self, jobID):
        pass
        
    def get_jobs(self, amount=None) -> dict:
        pass
    