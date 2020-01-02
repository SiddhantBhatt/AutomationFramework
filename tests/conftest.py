"""
Configuration file for running tests
"""

import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.yield_fixture()
# @pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
# @pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    """
    One Time Setup method
    Calls WebDriverFactory class and gets a driver instance
    One time login for all test cases
    returns/yields driver instance to the respective calling class
    """

    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.clickLoginLink()
    lp.login("test@email.com", "abcabc")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    """
    options/keywords to read values from terminal commands
    """
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    """
    returns value for --browser keyword
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    def osType(request):
        """
        returns value for --osType keyword
        """
    return request.config.getoption("--osType")
