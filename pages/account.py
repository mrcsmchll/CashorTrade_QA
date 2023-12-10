from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Account:
    URL = "https://front-stage.cashortrade.org/auth/account"
    USR_NAME = "usr69"
    USR_MAIL = USR_NAME + "@asd.com"
    #ids
    INPUT_USR = "input-text-account-register-username"
    INPUT_MAIL = "input-text-account-register-email"
    BTN_SUBMIT = "btn-username-phone-sign-up"
    BTN_SKIP_PIC = "btn-secondary-profile-pic-skip-for-now"
    CHECKBOX = ".flex:nth-child(3) > .cursor-pointer"

    def __init__(self, driver):
        self.driver = driver
    
    def create_user(self):
        self.driver.implicitly_wait(5)

        user_input = self.driver.find_element(By.ID, self.INPUT_USR)
        user_input.send_keys(self.USR_NAME)

        mail_input = self.driver.find_element(By.ID, self.INPUT_MAIL)
        mail_input.send_keys(self.USR_MAIL)

        #Accepting Terms of Service
        check_box = self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX)
        check_box.click()

        submit_button = self.driver.find_element(By.ID, self.BTN_SUBMIT)
        submit_button.click()

        #Skipping profile pic selection
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("profile-picture")
        )

        skip_pic = self.driver.find_element(By.ID, self.BTN_SKIP_PIC)
        skip_pic.click()