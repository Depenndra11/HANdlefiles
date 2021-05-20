from selenium import webdriver


class LoginPage:

    __username_field = "txtUsername"
    __password_field = "txtPassword"
    __login_button = "btnLogin"
    welcome_btn = "welcome"
    logout = select(welcome_btn)
    logout_btn = logout.select_by_text("logout")

    def __init__(self, driver):
        self.driver = driver

    def send_username(self, username):
        self.driver.find_element_by_id(self.__username_field).clear()
        self.driver.find_element_by_id(self.__username_field).send_keys(username)

    def send_password(self, password):
        self.driver.find_element_by_id(self.__password_field).clear()
        self.driver.find_element_by_id(self.__password_field).send_keys(password)

    def login_button(self):
        self.driver.find_element_by_id(self.__login_button).click()











