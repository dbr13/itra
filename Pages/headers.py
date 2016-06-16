from logging.handlers import TimedRotatingFileHandler
from webium.errors import WebiumException
from webium.driver import get_driver
from webium import Find, BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import logging

format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
logging.basicConfig(format=format, level=logging.INFO, filename='/home/dbr13/Itracker/Logs/dbr.log', filemode='a')
logger = logging.getLogger('Home_Page')
handler = TimedRotatingFileHandler(filename='/home/dbr13/Itracker/Logs/dbr.log', when="D", interval=1, backupCount=3)
logger.addHandler(handler)

class TextField(WebElement):
    @property
    def text(self):
        return self.get_attribute('value')


class Headers(BasePage):
    button_zapis = Find(by=By.XPATH, value=".//a[@class='zapisatsya']")

    def __init__(self):
        self.url = 'http://old.qalight.com/'
        self.__driver = webdriver.Chrome()
        #BasePage.__init__(self, url='http://oldqalight.com')
        BasePage._driver = self.__driver
        self._driver.maximize_window()

    def open_home_page(self):
        if not self.url:
            raise WebiumException('Can\'t open page without url')
        self.__driver.get(self.url)
        logger.info('open home page')

    def open_zapisatsya(self):
        try:
            window_before=self.__driver.window_handles[:]
            #print(window_before)
            self.button_zapis.click()
            window_after=self.__driver.window_handles[-1]
            #print(window_after)
            self.__driver.switch_to_window(window_after)
            self.close_page()
            self.__driver.switch_to_window(window_before[0])
        except Exception as exc:
            logger.error('open_zapisatsya: {0}'.format(exc))
            raise exc
        else:
            logger.info('open_zapisatsya')

    def close_page(self):
        self.__driver.close()

if __name__=='__main__':
    header = Headers()
    header.open_home_page()
    header.open_zapisatsya()