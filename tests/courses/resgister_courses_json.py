"""
Tests using ddt module for multiple data sets
"""

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack, file_data


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTestsJSON(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @file_data('registercoursesdata.json')
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV, postcode):
        """
        Tests for invalid enrollment by passing multiple wrong payment details
        Uses TestStatus class to mark/assert test case results
        """
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV, postcode=postcode)
        # result = self.courses.verifyEnrollFailed()
        result = True
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.driver.get("https://learn.letskodeit.com/")
