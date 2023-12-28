Feature: This enables the program to clear cache and logout

	Scenario: User logs out
		Given user logs in
		When user clears cache
		Then user becomes logged out
