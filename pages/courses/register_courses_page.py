"""
All the Courses page related methods will be present in this class
"""

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@name='cardnumber']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _postcode = "//input[@name='postal']"
    _savecardcheck = "save-payment-details"
    _tnccheck = "agreed_to_terms_checkbox"
    _submit_enroll = "//button[@id='confirm-purchase']"
    _enroll_error_message = "//div[@class='cc__error alert-danger']"
    # error message alternate xpath = //div[contains(text(),'The card was declined')]
    _ccnum_iframe = "//iframe[@name='__privateStripeFrame5']"
    _ccexp_iframe = "//iframe[@name='__privateStripeFrame6']"
    _cccvv_iframe = "//iframe[@name='__privateStripeFrame7']"
    _ccpostcode_iframe = "//iframe[@name='__privateStripeFrame8']"

    def enterCourseName(self, name):
        """
        Enter the course name in the course search box
        """

        self.nav.navigateToAllCourses()
        time.sleep(2)
        self.sendKeys(name, locator=self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        """
        Select the course from the name provided
        """
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        """
        Click on the enroll button
        """
        self.elementClick(locator=self._enroll_button)

    def enterCardNum(self, num):
        """
        Switch to card number iframe->field and enter card number
        """
        self.switchFrame(locator=self._ccnum_iframe, locatorType="xpath")
        self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.log.info("Entered card number")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        """
        Switch to card exp iframe->field and enter card exp
        """
        self.switchFrame(locator=self._ccexp_iframe, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.log.info("Entered card expiry")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        """
        Switch to card cvv iframe->field and enter card cvv
        """
        self.switchFrame(locator=self._cccvv_iframe, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.log.info("Entered CVV number")
        self.driver.switch_to.default_content()

    def enterPostcode(self, postcode):
        """
        Switch to postcode iframe->field and enter postcode
        """
        self.switchFrame(locator=self._ccpostcode_iframe, locatorType="xpath")
        self.sendKeys(postcode, locator=self._postcode, locatorType="xpath")
        self.log.info("Entered Postcode")
        self.driver.switch_to.default_content()

    def clickSaveCardCheck(self):
        """
        Click on Save card checkbox
        """
        self.elementClick(locator=self._savecardcheck)

    def clickTncCheck(self):
        """
        Click on T&C checkbox
        """
        self.elementClick(locator=self._tnccheck)

    def clickEnrollSubmitButton(self):
        """
        Click on Enroll Submit button
        """
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, postcode):
        """
        Enter credit card information in the form
        """
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPostcode(postcode)

    def enrollCourse(self, num="", exp="", cvv="", postcode=""):
        """
        Combines existing methods to complete course enrollment
        """
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv, postcode)
        self.clickSaveCardCheck()
        self.clickTncCheck()
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        """
        Verify error message for failed enrollment
        """
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
