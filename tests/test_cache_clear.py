import pytest
from DrissionPage import ChromiumPage
from pytest_bdd import parsers, scenario, given, when, then

from pages.homepage import homepage, clearCache
from pages.login import loginAccount

@pytest.fixture
def page():
    return ChromiumPage()

@scenario("features/cache.feature", "User logs out")
def test_clear_cache(page):
    page.clear_cache()
    page.quit()
    
@given("user logs in", target_fixture="login")    
def login(page):
    homepage(page)
    page.wait.load_start()
    loginAccount(page)

@when("user clears cache")
def clear_cache(page):
    page.wait.load_start()
    clearCache(page)
    
@then("user becomes logged out")
def check_homepage(page):
    homepage(page)
    page.wait.load_start()
    assert not "https://www.linkedin.com/feed/" in page.url