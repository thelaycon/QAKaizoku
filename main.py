import json

import click
from DrissionPage import WebPage, ChromiumOptions

from pages.homepage import homepage
from pages.login import loginAccount


@click.group()
def linkedinScrape():
    pass
    
@linkedinScrape.command()
@click.option("--headless", default=1, help="Run Chrome browser in headless mode")
def login(headless):
   
    # Set options
    co = ChromiumOptions()
    
    # Configure headless mode
    if headless == 0:
        co.headless(False)
    else:
        co.headless(True)
        
    page = WebPage(chromium_options=co)

    # Navigate to homepage
    home = homepage(page)
    
    # Login account
    loginAccount(home)

    page.quit()
    
if __name__ == "__main__":

    linkedinScrape()
