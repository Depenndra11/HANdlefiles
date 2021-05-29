from selenium import webdriver
from pages.adduser import AddUser
import logging
from utilities.coustomlogger import LogGen
from pages.login_page import LoginPage


class TestAddUser:
    def __init__(self, setup):
        baseurl = ReadConfig.getUrl()
        username = ReadConfig.getuserName()
        password = ReadConfig.getpassword()
        logger = LogGen.loggen()





