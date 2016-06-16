from selenium import webdriver
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox_capabilities=DesiredCapabilities.FIREFOX
firefox_capabilities['marionette']=True
firefox_capabilities['binary']='/home/dbr13/MyVenv/geckodriver-0.8.0-linux64'

class Test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test1(self):
        self.driver.get("http://itracker.com.ua")
        self.driver.implicitly_wait(30)
        driver = WebDriverWait(driver=self.driver,timeout=30).until(EC.element_to_be_clickable((By.XPATH, ".//li[@id='menu-item-38']/a")))
        self.driver.find_element_by_xpath(".//li[@id='menu-item-38']/a").click()

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()