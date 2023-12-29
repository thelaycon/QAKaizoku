# QAKaizoku API - QA Automation Jobs

QAKaizoku is an API crafted for QA Automation jobs from LinkedIn. This project is under active development, with continuous enhancements being made to ensure optimal performance and reliability.

## Overview

QAKaizoku is a tool designed to automate the extraction of QA Automation job listings from LinkedIn. The core functionality is encapsulated in `main.py`, serving as the central entry point for scraping data. This script seamlessly logs into the LinkedIn website undetected, providing a streamlined approach to retrieving job information.

## Usage

Before diving in, it is recommended to execute the application in a non-headless mode during the initial login. This facilitates the bot in solving challenges and establishing trust with LinkedIn. Once the inaugural login is successful, subsequent runs can be executed in headless mode, enabling the bot to navigate through the feed page without detection.

### Scraping Commands

To facilitate automation and regular updates, the scraping commands can be scheduled using cron jobs. Below are the modified commands suitable for cron jobs:

- To initiate the login bot in non-headless mode:
  ```bash
  python main.py login --headless=0
  ```

- To clear the cache for a fresh login attempt:
  ```bash
  python main.py clear
  ```

- To commence the scraping process every hour:
  ```bash
  0 * * * * cd /path/to/QAKaizoku && python main.py run
  ```


### Additional Notes

- If you have previously logged in via Chrome and are attempting a new login, ensure that the browser cache is cleared.

- By default, the bot operates in headless mode. Customization of job scraping options can be achieved through the `options.json` file.

## Customizing Job Options

Tailor the job scraping process to your specifications by modifying the `options.json` file. A sample configuration is provided below:

```json
{
	"home": "https://www.linkedin.com/",
	"geoid": "103644278",
	"keyword": "QA Automation",
	"location": "United States"
}
```

Feel free to adjust parameters such as `keyword` and `location` to align with your specific requirements.

The application now integrates Firebase for data storage. Configure the Firebase JSON file or implement credentials accordingly. The database URL is fetched from the environment as DATABASE_URL.


## API Endpoints

To access the jobs API, ensure the FastAPI program is running:

```bash
uvicorn api:app --reload
```

Available endpoints:

- Get jobs: `/jobs`

[!get jobs](examples/example_get_jobs.png)