from selenium.webdriver.common.by import BY

class Home:
    #ids
    BTN_LOGIN_DESKTOP = "btn-secondary-log-in"
    BTN_LOGIN_MOBILE = "mobile-footer-login"

    def __init__(self, driver):
        self.driver = driver

    def click_login_desktop(self):
        self.driver.find_element(BY.ID, self.BTN_LOGIN_DESKTOP).click()

    def click_login_mobile(self):
        self.driver.find_element(BY.ID, self.BTN_LOGIN_MOBILE).click()


