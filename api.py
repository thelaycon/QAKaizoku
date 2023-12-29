from fastapi import FastAPI

from firebase.database import Database


app = FastAPI()
Database = Database()


@app.get("/jobs")
def getJobs():
    data = Database.getjobsFromFirebase()
    return data
