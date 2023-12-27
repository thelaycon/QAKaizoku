import os
import json
from dotenv import load_dotenv
from DrissionPage import ChromiumPage

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def loginAccount(page: ChromiumPage) -> ChromiumPage:
    page.set.window.maximized()
    # Attempt to login LinkedIn with ChromiumPage

    with open("urls.json") as file:
        urls = json.load(file)

    homeUrl = urls["home"]
    page.get(homeUrl)
    page.ele("@data-tracking-control-name=guest_homepage-basic_nav-header-signin").click()

    page.wait.load_start()

    page.ele("@id=username").input(EMAIL)
    page.ele("@id=password").input(PASSWORD + "\n")

p = ChromiumPage()
loginAccount(p)
