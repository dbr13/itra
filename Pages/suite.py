import unittest
from teamcity.unittestpy import TeamcityTestRunner
from teamcity import is_running_under_teamcity
from Pages.test_suite_home_page import TestSuiteHomePage
from Pages.test_suite_zapisatsya_page import TestSuiteZapisatsyaPage
from teamcity.unittestpy import TeamcityServiceMessages

def suite():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSuiteHomePage)
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSuiteZapisatsyaPage))
    return unittest.TestSuite([suite])

def run(suite):
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__=='__main__':
    run(suite())

