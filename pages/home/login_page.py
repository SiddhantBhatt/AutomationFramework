"""
All the Login page related methods will be present in this class
"""

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    def clickLoginLink(self):
        """
        Click on the Login link
        """
        self.elementClick(self._login_link, locatorType="link")

    def clearFields(self):
        """
        Clear email and password fields
        """
        self.clearField(self._email_field, locatorType="id")
        self.clearField(self._password_field, locatorType="id")

    def enterEmail(self, email):
        """
        Enter email in the email field
        """
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        """
        Enter password in the password field
        """
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        """
        Click on the login(form) button
        """
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email="", password=""):
        """
        Combines methods to execute login flow
        """
        time.sleep(5)
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        """
        Verify if the login was successful
        """
        self.waitForElement("//input[@id='search-courses']", locatorType="xpath")
        result = self.isElementPresent("//input[@id='search-courses']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        """
        Verify if the login failed
        """
        self.waitForElement("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        """
        Verify Page title
        """
        return self.verifyPageTitle("Let's Kode It")

    def logout(self):
        """
        Method to log out
        """
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//div[@id='navbar']//a[@href='/sign_out']",
                                                locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@id='navbar']//a[@href='/sign_out']",
                          locatorType="xpath")