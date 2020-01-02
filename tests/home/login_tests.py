"""
Tests for Login Page
"""

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t1invalidLogin(self):
        """
        Tests for invalid login test case
        Logs out first because of oneTimeSetup Login
        """
        self.log.info("*#" * 20)
        self.log.info("test_t1invalidLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.clickLoginLink()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_t2validLogin(self):
        """
        Tests for valid login test case
        Also tests for Login Title
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_t2validLogin started")
        self.log.info("*#" * 20)
        self.lp.logout()
        self.lp.clickLoginLink()
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_t2validLogin", result2, "Login Verification")