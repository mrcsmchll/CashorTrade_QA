from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home:
    URL = "https://front-stage.cashortrade.org/"
    #ids
    BTN_LOGIN_DESKTOP = (By.ID, "btn-secondary-log-in")
    BTN_LOGIN_MOBILE =(By.ID, "mobile-footer-login") 
    BTN_SELL_TICKET_1 =(By.ID, "opt-2-sell-my-tickets") 
    BTN_SELL_TICKET_2 =(By.ID, "homepage-sell") 
    #tag loc
    OVERLAY_LOC = (By.ID, "overlay")
    FORM_LOC = (By.CLASS_NAME, "relative h-full bg-white rounded-t-3xl")

    CALL_TIMEOUT = 10
    
    def __init__(self, driver):
        self.driver = driver

    def click_login_desktop(self):
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.element_to_be_clickable(self.BTN_LOGIN_DESKTOP)
        )
        self.driver.find_element(*self.BTN_LOGIN_DESKTOP).click()
       
    def click_login_mobile(self):
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.element_to_be_clickable(self.BTN_LOGIN_MOBILE)
        )
        self.driver.find_element(*self.BTN_LOGIN_MOBILE).click()

    def click_login_sell_ticket(self):
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.element_to_be_clickable(self.BTN_SELL_TICKET_1)
        )
        self.driver.find_element(*self.BTN_SELL_TICKET_1).click()
       
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.element_to_be_clickable(self.BTN_SELL_TICKET_2)
        )
        self.driver.find_element(*self.BTN_SELL_TICKET_2).click()
       

