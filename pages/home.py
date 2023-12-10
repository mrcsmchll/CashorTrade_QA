from selenium.webdriver.common.by import By

class Home:
    URL = "https://front-stage.cashortrade.org/"
    #ids
    BTN_LOGIN_DESKTOP = "btn-secondary-log-in"
    BTN_LOGIN_MOBILE = "mobile-footer-login"
    OVERLAY_LOC = (By.ID, "overlay")
    
    def __init__(self, driver):
        self.driver = driver

    def click_login_desktop(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_LOGIN_DESKTOP).click()
       
    def click_login_mobile(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_LOGIN_MOBILE).click()
       

