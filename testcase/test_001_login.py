from selenium import webdriver
from pages.login_page import LoginPage
import pytest
from utilities.readProperties import ReadConfig
import logging
from utilities.coustomlogger import LogGen




class TestLogin:
    baseurl = ReadConfig.getUrl()
    username = ReadConfig.getuserName()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_001_login(self, setup):
        self.logger.info("*******test__001__login started")
        self.driver = setup
        self.driver.get(self.baseurl)
        act = self.driver.title
        if act == "OrangeRM":
            assert True
            self.driver.close()
            self.logger.info("******loin__001__test passed ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_001_login.png")
            title = self.driver.title
            print(title)
            self.driver.close()
            self.logger.error("******loin__001__test failed ")
            assert False

    def test_002_login(self, setup):
        self.logger.info("******loin__002__test started ")

        self.driver = setup
        self.driver.get(self.baseurl)
        lp = LoginPage(self.driver)
        lp.send_username(self.username)
        lp.send_password(self.password)
        lp.login_button()
        self.driver.close()
        self.logger.info("******loin__001__test passed ")



