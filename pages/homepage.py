import json
from DrissionPage import ChromiumPage

def homepage(page: ChromiumPage) -> ChromiumPage:
    page.set.window.maximized()
    # Attempt to login LinkedIn with ChromiumPage

    with open("options.json") as file:
        options = json.load(file)

    homeUrl = options["home"]
    page.get(homeUrl)
    
    return page


def clearCache(page: ChromiumPage) -> ChromiumPage:
    page.clear_cache()
    return page