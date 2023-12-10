from selenium.webdriver.common.by import By


class Auth:
    AUTH_CODE = "000000" 
    #ids
    INPUT_CODE = "input-confirmation-code"
    BTN_SUBMIT = "btn-sign-up-phone-number-next"

    def __init__(self, driver):
        self.driver = driver

    def verify_phone(self):
        self.driver.implicitly_wait(5)
        
        auth_code_input = self.driver.find_element(By.ID,self.INPUT_CODE)
        auth_code_input.send_keys(self.AUTH_CODE)
        
        submit_button = self.driver.find_element(By.ID, self.BTN_SUBMIT)
        submit_button.click()
        