from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    URL = "https://front-stage.cashortrade.org/auth/register"
    #ids
    INPUT_PHONE = (By.ID, "input-tel-sign-up-phone-number")
    BTN_SUBMIT = "btn-sign-up-phone-number-next"
    
    def __init__(self, driver):
        self.driver = driver

    def login_with_phone_num(self, phone):
        WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(self.INPUT_PHONE)
        )

        phone_input = self.driver.find_element(*self.INPUT_PHONE)
        phone_input.send_keys(phone)
        
        submit_button = self.driver.find_element(By.ID, self.BTN_SUBMIT)
        submit_button.click()
        