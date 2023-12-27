Feature: Scraper logins to Linkedin account without detection

	Scenario: User logs in
		Given: the homepage is opened
		And: the login button is clicked
		When: the login form is filled
		And: the login button is clicked
		Then: user should be logged in successfully
