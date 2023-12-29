# QAKaizoku API - LinkedIn QA Automation Job Scraper

Welcome to QAKaizoku, an API designed for QA Automation job scraping from LinkedIn. Please note that this project is currently in development, and improvements are actively being made.

## Overview

QAKaizoku serves as a tool for automating the retrieval of QA Automation job listings from LinkedIn. The primary functionality is housed in `main.py`, the entry point of the application. The script attempts to log in to the LinkedIn website undetected, providing seamless access to relevant job information.

## Usage

Before you begin, it's recommended to run the application in a non-headless mode for the initial login. This enables the bot to solve challenges and establish trust with LinkedIn. Once the initial login is successful, subsequent runs can be executed in headless mode, allowing the bot to navigate through the feed page undetected.

### Commands

- To initiate the login bot in non-headless mode:
  ```bash
  python main.py login --headless=0
  ```

- To clear the cache for a fresh login attempt:
  ```bash
  python main.py clear
  ```

- To start the scraping process:
  ```bash
  python main.py run
  ```

### Additional Notes

- If you have logged in via Chrome before and are attempting a new login, ensure that the browser cache is cleared.

- By default, the bot runs headlessly. You can customize job scraping options through the `options.json` file.

## Customizing Job Options

Modify the `options.json` file to tailor the job scraping process to your preferences. Example configuration:

```json
{
	"home": "https://www.linkedin.com/",
	"geoid": "103644278",
	"keyword": "QA Automation",
	"location": "United States",
}
```

Feel free to adjust parameters such as `keyword`, `location`, and `headless` to suit your specific requirements.