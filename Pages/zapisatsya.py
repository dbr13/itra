from logging.handlers import TimedRotatingFileHandler

from webium import Find, BasePage
import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

format = '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
logging.basicConfig(format=format, level=logging.INFO, filename='/home/dbr13/Itracker/Logs/dbr.log', filemode='a')
logger = logging.getLogger('Zapisatsya_Page')
handler = TimedRotatingFileHandler(filename='/home/dbr13/Itracker/Logs/dbr.log', when="D", interval=1, backupCount=3)
logger.addHandler(handler)

class TextField(WebElement):
    @property
    def text(self):
        return self.get_attribute('value')

class Zapisatsya(BasePage):
    dd_course = Find(by=By.NAME, value='menu-11')
    last_name = Find(TextField, By.NAME, 'your-name')
    first_name = Find(TextField, By.NAME, 'text-68')
    phone = Find(TextField, By.NAME, 'text-297')
    mail = Find(TextField, By.NAME, 'your-email')
    skype = Find(TextField, By.NAME, 'text-71')
    button_kupit = Find(by=By.XPATH, value=".//input[@type='submit']")
    validation_error = Find(by=By.XPATH, value=".//*[contains(@class,'validation-errors')]")
    success_msg = Find(by=By.XPATH, value=".//div[contains(@class,'mail-sent-ok')]")

    def __init__(self):
        self.url = 'http://old.qalight.com/zapisatsya-na-kurs/'
        self.__driver = webdriver.Chrome()
        BasePage._driver = self.__driver
        self.__driver.maximize_window()


    def open(self):
        BasePage.open(self)

    def select_dd_course(self, course):
        try:
            dd_element = Select(self.dd_course)
            dd_element.select_by_value(course)
            logger.info('Corse {0} was selected' .format(course))
        except Exception as exc:
            logger.error('dd_course - {0}' .format(exc))
            raise exc

    def type_last_name(self, name):
        try:
            self.last_name.clear()
            self.last_name.send_keys(name)
            logger.info('Lastname {0} was typed'.format(name))
        except Exception as exc:
            logger.error('last_name {0}'.format(exc))
            raise exc

    def error_message(self):
        self.is_element_present('validation_error')
        print('elements is present: {0}'.format(self.validation_error.text))

    def click_button_kupit(self):
        self.button_kupit.click()

    def type_first_name(self, name):
        self.first_name.clear()
        self.first_name.send_keys(name)

    def type_phone(self, phone):
        self.phone.clear()
        self.phone.send_keys(phone)

    def type_email(self, mail):
        self.mail.clear()
        self.mail.send_keys(mail)

    def type_skype(self, skype):
        self.skype.clear()
        self.skype.send_keys(skype)

    def success_message(self):
        try:
            a = self.success_msg
            a.is_displayed()
            logger.info('Success message is: {0}'.format(self.success_msg.text))
        except Exception as exc:
            logger.error('Success_message - {0}'.format(exc))
            raise exc

    def close_page(self):
        self.__driver.close()


if __name__=='__main__':
    A = Zapisatsya()
    A.open()