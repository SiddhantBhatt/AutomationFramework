"""
Class containing basic navigation methods in the ome page
"""

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"

    def navigateToAllCourses(self):
        """
        Navigate/Click on All courses link/page
        """
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        """
        Navigate/Click on My Courses link/page
        """
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        """
        Navigate/Click on Practice link/page
        """
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        """
        Navigate/click to User settings section
        """
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")
