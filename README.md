# QAKaizoku API - LinkedIn QA Automation Job Scraper

Welcome to QAKaizoku, an advanced API meticulously crafted for QA Automation job scraping from LinkedIn. This cutting-edge project is under active development, with continuous enhancements being made to ensure optimal performance and reliability.

## Overview

QAKaizoku is a sophisticated tool designed to automate the extraction of QA Automation job listings from LinkedIn. The core functionality is encapsulated in `main.py`, serving as the central entry point for the application. This script seamlessly logs into the LinkedIn website undetected, providing a streamlined approach to retrieving pertinent job information.

## Usage

Before diving in, it is recommended to execute the application in a non-headless mode during the initial login. This facilitates the bot in solving challenges and establishing trust with LinkedIn. Once the inaugural login is successful, subsequent runs can be executed in headless mode, enabling the bot to navigate through the feed page without detection.

### Commands

- To initiate the login bot in non-headless mode:
  ```bash
  python main.py login --headless=0
  ```

- To clear the cache for a fresh login attempt:
  ```bash
  python main.py clear
  ```

- To commence the scraping process:
  ```bash
  python main.py run
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

Feel free to adjust parameters such as `keyword`, `location`, and `headless` to align with your specific requirements.

The application now integrates Firebase for data storage. Configure the Firebase JSON file or implement credentials accordingly. The database URL is fetched from the environment as DATABASE_URL.