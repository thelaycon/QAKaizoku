import logging
import json
import re
from urllib import parse

from DrissionPage import ChromiumPage

from firebase.database import Database

Database = Database()

JOBS_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3795202306&f_TPR=r604800&geoId={0}&keywords={1}&location={2}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD"

def getJobData(page: ChromiumPage, url: str) -> dict:
    page.get(url)
    page.wait.load_complete()
    
    #Get the data
    jobID = re.search(r"/(\d+)/", page.url).group(1)
    
    # Get individual detail
    jobDetail = page.ele("@class=job-details-jobs-unified-top-card__primary-description-without-tagline mb2").texts()
    jobDetailJoined = "".join(jobDetail)
    
    company, locationTime, applicants = jobDetailJoined.split("·") 
    
    if "just now" in locationTime:
        time = "just now"
        location = locationTime.strip("just now")
    else:    
        pattern = re.compile(r"(\d+)\s+(hour|day|week|minute|month|year)s?\s+ago")
        time = pattern.search(locationTime).group()
        location = re.sub(pattern, "", locationTime)
    jobDescription = page.ele("@id=job-details").inner_html
    
    return {
        "jobID": jobID,
        "detail": {
            "company": company,
            "time": time,
            "location": location,
            "jobDescription": jobDescription
            }
        }
    
    
def saveJobs(page: ChromiumPage, links: list) -> bool:
    
    data = dict()
    try:
        for link in links:
            jobData = getJobData(page, link)
            Database.saveJobsToFirebase(jobData)
    except:
        logging.warning("Unable to get detail for a job, skipping")
    
    
    
    
def scrapeJobs(page: ChromiumPage) -> ChromiumPage:
    page.set.window.maximized()
    
    with open("options.json") as file:
        options = json.load(file)
        
    GEOID = options["geoid"]
    KEYWORD = options["keyword"]
    LOCATION = options["location"]
    
    URL = JOBS_URL.format(GEOID, parse.quote(KEYWORD), parse.quote(LOCATION))
    
    # Visit jobs page
    page.get(URL)
    page.wait.load_complete()
    
    jobs = page.eles("@class=disabled ember-view job-card-container__link job-card-list__title")
    jobLinks = [job.link for job in jobs]
    
    saveJobs(page, jobLinks) #Save jobs to firebase
    
    
    
    