from selenium.webdriver.common.by import By

class Home:
    URL = "https://front-stage.cashortrade.org/"
    #ids
    BTN_LOGIN_DESKTOP = "btn-secondary-log-in"
    BTN_LOGIN_MOBILE = "mobile-footer-login"
    BTN_SELL_TICKET_1 = "opt-2-sell-my-tickets"
    BTN_SELL_TICKET_2 = "homepage-sell"
    #tag loc
    OVERLAY_LOC = (By.ID, "overlay")
    FORM_LOC = (By.CLASS_NAME, "relative h-full bg-white rounded-t-3xl")

    def __init__(self, driver):
        self.driver = driver

    def click_login_desktop(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_LOGIN_DESKTOP).click()
       
    def click_login_mobile(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_LOGIN_MOBILE).click()

    def click_login_sell_ticket(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_SELL_TICKET_1).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_SELL_TICKET_2).click()
       

