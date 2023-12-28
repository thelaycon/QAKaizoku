# QAKaizoku

QAKaizoku is an API for QA Automation jobs scraped from LinkedIn, however, still in development. Currently, the entry point is at main.py which attempts to login to the LinkedIn website undedected.

When running for the first time or trying to login, it should be ran in a non-headless mode to be able to solve challenges and establish trust. Thereafter, the bot can enter the feed page undedected using Chrome in a headless mode. 
If you have once logged in via Chrome before and you are attempting a new login, ensure that the cache is cleared. 

Login bot:

`python main.py login --headless=0`

Clear cache:

`python main.py clear`

Start scraping

`python main.py run`


Defautly, the bot run headlessly.