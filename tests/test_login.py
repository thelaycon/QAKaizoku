import pytest
from DrissionPage import ChromiumPage
from pytest_bdd import parsers, scenario, given, when, then

from pages.homepage import homepage
from pages.login import loginAccount

@pytest.fixture
def page():
    return ChromiumPage()

@scenario("features/login.feature", "User logs in")
def test_linkedIn_login(page):
    page.clear_cache()
    page.quit()
    
@given("the homepage is opened", target_fixture="home")
def home(page):
    return homepage(page)
    
@when("the login form is filled and clicked")
def login(home):
    loginAccount(home)

@then("user should be logged in successfully")
def atHome(home):
    home.wait.load_start()
    assert "https://www.linkedin.com/feed/" in home.url