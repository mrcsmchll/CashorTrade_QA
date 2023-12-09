from selenium.webdriver.common.by import By


class Auth:
    AUTH_CODE = "000000" 
    #ids
    INPUT_CODE = "input-confirmation-code"
    BTN_SUBMIT = "btn-sign-up-phone-number-next"

    def __init__(self) -> None:
        pass

    def verify_phone(self):
        #TODO
        # auth_code_input = self.driver.find_element(By.ID, )
        # auth_code_input.send_keys(Utils.AUTH_CODE)
