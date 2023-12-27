Feature: Scraper logins to Linkedin account without detection

	Scenario: User logs in
		Given the homepage is opened
		When the login form is filled and clicked
		Then user should be logged in successfully
