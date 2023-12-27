from DrissionPage import ChromiumPage
from pytest_bdd import parsers, scenario, given, when, then

from login import loginAccount

@scenario("features/login.feature", "Scraper logins to Linkedin account without detection")
def test_linkedIn_login():
    pass
    
    
@given("the homepage is opened", target_fixture="homepage"):
def homepage():
    p = ChromiumPage()
    loginAccount(p)
    
@when("the login form is filled and clicked")
 def login():
    pass

@then("user should be logged in successfully"):
def atHome():
    pass