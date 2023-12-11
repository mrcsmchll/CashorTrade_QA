from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class Account:
    URL = "https://front-stage.cashortrade.org/auth/account"
   
    #ids
    CHECKBOX = ".flex:nth-child(3) > .cursor-pointer"
    INPUT_USR = "input-text-account-register-username"
    INPUT_MAIL = "input-text-account-register-email"
    BTN_SUBMIT = "btn-username-phone-sign-up"
    BTN_SKIP_PIC = "btn-secondary-profile-pic-skip-for-now"
    BTN_SELL = "btn-sell-tickets-header"
    BTN_SKIP_WLK = (By.ID, "btn-secondary-walkthrough-skip")
    WALLET_WRAPPER = (By.ID, "ticket-wallet-wrapper")


    def __init__(self, driver):
        self.driver = driver
    
    def create_user(self, name, mail):

        self.driver.implicitly_wait(5)

        user_input = self.driver.find_element(By.ID, self.INPUT_USR)
        user_input.send_keys(name)

        mail_input = self.driver.find_element(By.ID, self.INPUT_MAIL)
        mail_input.send_keys(mail)

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

    def skip_walkthrough(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BTN_SKIP_WLK)
        )
        self.driver.find_element(*self.BTN_SKIP_WLK).click()

    def sell_ticket(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, self.BTN_SELL).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.WALLET_WRAPPER)
        )    

        performers = self.driver.find_elements(By.CLASS_NAME, "space-y-3.transform.translate-y-0.hoist-undefined.svelte-1xzbzxf")
        perfs_with_event = []

       for i, performer in enumerate(performer s):
            try:
                self.driver.find_element(By.ID, "performer-result-" + str(i)).click()
                self.driver.implicitly_wait(2)

                # Check if there is a nested element with ID "search-event-result-0"
                try:
                    nested_element = self.driver.find_element(By.ID, "search-event-result-0")
                    perfs_with_event.append(nested_element)
                except NoSuchElementException:
                    pass  # No nested element found, continue with the next performer
            except StaleElementReferenceException:
                print(f"Element at index {i} became stale. Skipping.")
            continue

            
        if perfs_with_event:        
        #select the first performer found that has registered an event
            perfs_with_event[0].click()
            self.driver.implicitly_wait(2)

            event = self.driver.find_element(By.ID, "search-event-result-0")
            event.click()
            self.driver.implicitly_wait(2)

            sell_btn = self.driver.find_element(By.ID, "sellortrade-sell")
            sell_btn.click()
            self.driver.implicitly_wait(2)

            digital_transfer_btn = self.driver.find_element(By.ID, "relative rounded-lg px-4.5 py-3 group  svelte-1i2ok0t")
            digital_transfer_btn.click()
            self.driver.implicitly_wait(2)


            submit_btn = self.driver.find_element(By.ID, "btn-create-listing-transferType")
            submit_btn.click()
            self.driver.implicitly_wait(2)

            quantity_dropdown = self.driver.find_element(By.ID, "input-dropdown-quantity-select")
            quantity_dropdown.click()
            self.driver.implicitly_wait(2)

            quantity_amount_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            quantity_amount_1.click()
            self.driver.implicitly_wait(2)

            ready_btn = self.driver.find_element(By.ID, "btn-selector-ready")
            ready_btn.click()
            self.driver.implicitly_wait(2)

            og_purchase = self.driver.find_element(By.ID, "input-dropdown-ticket-wallet-primary-vendor")
            og_purchase.click()
            self.driver.implicitly_wait(2)

            og_purchase_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            og_purchase_1.click()
            self.driver.implicitly_wait(2)

            ticket_info = self.driver.find_element(By.ID, "btn-selector-general-admission")
            ticket_info.click()
            self.driver.implicitly_wait(2)

            ticket_loc_dropdown = self.driver.find_element(By.ID, "input-dropdown-ticket-wallet-ga-section")
            ticket_loc_dropdown.click()
            self.driver.implicitly_wait(2)

            ticket_loc_selection =  self.driver.find_element(By.ID, "input-dropdown-option-7")
            ticket_loc_selection.click()
            self.driver.implicitly_wait(2)

            submit_btn = self.driver.find_element(By.ID, "btn-create-listing-mediumSpecificInfo")
            submit_btn.click()
            self.driver.implicitly_wait(5)

            price_input = self.driver.find_element(By.ID, "input-number-create-listing-price-per")
            price_input.send_keys("12")

            face_value_radio = self.driver.find_element(By.NAME, "Face Value")
            face_value_radio.click()

            submit_btn = self.driver.find_element(By.ID, "btn-create-listing-ticketPricing")
            submit_btn.click()
            self.driver.implicitly_wait(5)

            add_payment = self.driver.find_element(By.ID, "block w-full sm:w-auto rounded-lg border-2 border-primary border-solid px-6 py-3 relative flex justify-center items-center svelte-1cvyoxz")
            add_payment.click()
            self.driver.implicitly_wait(5)

            card_number_input = self.driver.find_element(By.ID, "Field-numberInput")
            card_number_input.send_keys("4242424242424242")

            expiration_number_input = self.driver.find_element(By.ID, "Field-expiryInput")
            month = datetime.today().month
            year = datetime.today().year + 1        
            expiration_number_input.send_keys(month + year)

            cvc_input = self.driver.find_element(By.ID, "Field-cvcInput")
            cvc_input.send_keys("123")

            name_input = self.driver.find_element(By.ID, "Field-nameInput")
            name_input.send_keys("some_name")

            address_input = self.driver.find_element(By.CLASS_NAME, "Field-addressLine1Input")
            address_input.send_keys("some_address")

            submit_btn = self.driver.find_element(By.ID, "btn-submit")
            submit_btn.click()
            self.driver.implicitly_wait(5)

            next_btn = self.driver.find_element(By.ID, "btn-create-listing-creditCardInformation")
            next_btn.click()
            self.driver.implicitly_wait(5)
        else:
            raise NoPerformersWithEventsError("No performers with events found.")

class NoPerformersWithEventsError(Exception):
    pass


        
