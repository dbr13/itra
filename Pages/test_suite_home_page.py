import unittest
from logging.handlers import TimedRotatingFileHandler
import logging
from Pages.headers import Headers
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from webium.driver import get_driver

format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
logging.basicConfig(format=format, level=logging.INFO, filename='/home/dbr13/Itracker/Logs/dbr.log', filemode='a')
logger = logging.getLogger('Test_suite_HomePage')
handler = TimedRotatingFileHandler(filename='/home/dbr13/Itracker/Logs/dbr.log', when="D", interval=1, backupCount=3)
logger.addHandler(handler)

class TestSuiteHomePage(unittest.TestCase, Headers):
    def setUp(self):
        self.home = Headers()

    def tearDown(self):
        self.home.close_page()

    def test_button_zapisatsya(self):
        try:
            self.home.open_home_page()
            self.home.open_zapisatsya()
            logger.info('{0} - {1}'.format(self._testMethodName, 'Passed'))
        except Exception as exc:
            logger.error('{0} - {1}'.format(self._testMethodName, 'Failed'))
            raise exc

if __name__=='__main__':
    unittest.main()



