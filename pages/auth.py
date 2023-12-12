from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Auth:
    AUTH_CODE = "000000" 
    #ids
    INPUT_CODE = (By.ID, "input-confirmation-code")
    BTN_NEXT = (By.ID, "btn-sign-up-phone-number-next")
    
    CALL_TIMEOUT = 6

    def __init__(self, driver):
        self.driver = driver

    def verify_phone(self):
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.visibility_of_element_located(self.INPUT_CODE)
        )
        auth_code_input = self.driver.find_element(*self.INPUT_CODE)
        auth_code_input.send_keys(self.AUTH_CODE)
        
        next_button = self.driver.find_element(*self.BTN_NEXT)
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.element_to_be_clickable(self.BTN_NEXT)
        )
        next_button.click()
        