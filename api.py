from fastapi import FastAPI

from firebase.database import Database


app = FastAPI()
Database = Database()


@app.get("/jobs")
def getJobs(limit: int=None):
    data = Database.getJobsFromFirebase(limit)
    return data
