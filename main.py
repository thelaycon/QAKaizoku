from DrissionPage import ChromiumPage

from pages.homepage import homepage
from pages.login import loginAccount


def getJobs(page: ChromiumPage) -> ChromiumPage:
    # Navigate to homepage
    home = homepage(page)
    
    # Login account
    loginAccount(home)
    
if __name__ == "__main__":
    p = ChromiumPage()
    getJobs(p)