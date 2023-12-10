from selenium.webdriver.common.by import By
from utils.utils import Utils

class Login:
    #ids
    INPUT_PHONE = "input-tel-sign-up-phone-number"
    BTN_SUBMIT = "btn-sign-up-phone-number-next"
    
    def __init__(self, driver):
        self.driver = driver

    def login_with_phone(self):
        phone_input = self.driver.find_element(By.ID, self.INPUT_PHONE)
        phone_input.send_keys(Utils.random_phone_number())
        
        submit_button = self.driver.find_element(By.ID, self.BTN_SUBMIT)
        submit_button.click()
        