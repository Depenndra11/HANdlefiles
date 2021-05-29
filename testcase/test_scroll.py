from selenium import webdriver
from pages.login_page import LoginPage
from utilities.readProperties import ReadConfig
import logging
from utilities.coustomlogger import LogGen
import time

class TestScroll:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getuserName()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_Scroll(self, setup):
        self.logger.info("*******test__scroll started")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.scroll = LoginPage(self.driver)
        self.scroll.send_username(self.username)
        self.scroll.send_password(self.password)
        self.scroll.login_button()



        self.driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, -700);")
        time.sleep(3)

        self.scroll.logout_user()
        self.driver.close()
        logging.info("#######test scroll succesfull#####")







