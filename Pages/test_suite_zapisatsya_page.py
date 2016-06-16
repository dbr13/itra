import unittest
from logging.handlers import TimedRotatingFileHandler
import logging
from Pages.zapisatsya import Zapisatsya
from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner
from webium.driver import get_driver

format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
logging.basicConfig(format=format, level=logging.INFO, filename='/home/dbr13/Itracker/Logs/dbr.log', filemode='a')
logger = logging.getLogger('Test_suite_ZapisatsyaPage')
handler = TimedRotatingFileHandler(filename='/home/dbr13/Itracker/Logs/dbr.log', when="D", interval=1, backupCount=3)
logger.addHandler(handler)

class TestSuiteZapisatsyaPage(unittest.TestCase, Zapisatsya):
    def setUp(self):
        self.zapis = Zapisatsya()

    def tearDown(self):
        self.zapis.close_page()

    def test_get_success_msg(self):
        try:
            self.zapis.open()
            self.zapis.select_dd_course('Android')
            self.zapis.type_email('dober.uk@gmail.com')
            self.zapis.type_first_name('Denys')
            self.zapis.type_last_name('DDD')
            self.zapis.type_phone('0933559988')
            self.zapis.type_skype('d.bortovets')
            self.zapis.click_button_kupit()
            self.success_message()
            logger.info('{0} - {1}'.format(self._testMethodName, 'Passed'))
        except Exception as exc:
            logger.error('{0} - {1}'.format(self._testMethodName, 'Failed'))
            raise exc

if __name__=='__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
