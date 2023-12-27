import json
from DrissionPage import ChromiumPage

def homepage(page: ChromiumPage) -> ChromiumPage:
    page.set.window.maximized()
    # Attempt to login LinkedIn with ChromiumPage

    with open("urls.json") as file:
        urls = json.load(file)

    homeUrl = urls["home"]
    page.get(homeUrl)
    
    return page