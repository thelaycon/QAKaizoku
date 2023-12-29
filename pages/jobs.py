from urllib import parse
import json

from DrissionPage import ChromiumPage

JOBS_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3795202306&f_TPR=r604800&geoId={0}&keywords={1}&location={2}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD"

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
    job_links = [job.link for job in jobs]
    
    
    