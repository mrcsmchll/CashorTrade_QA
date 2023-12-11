from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from utils.user import User

class Account:
    URL = "https://front-stage.cashortrade.org/auth/account"
   
    #ids
    CHECKBOX = ".flex:nth-child(3) > .cursor-pointer"
    INPUT_USR = (By.ID, "input-text-account-register-username")
    INPUT_MAIL = "input-text-account-register-email"
    BTN_SUBMIT = "btn-username-phone-sign-up"
    BTN_SKIP_PIC = "btn-secondary-profile-pic-skip-for-now"
    BTN_SELL = "btn-sell-tickets-header"
    BTN_SKIP_WLK = (By.ID, "btn-secondary-walkthrough-skip")
    BTN_EVENT = (By.ID, "search-event-result-0")
    BTN_EVENT_SELL = (By.ID, "sellortrade-sell")
    BTN_DIGITAL_TRANSF = (By.CSS_SELECTOR, ".relative:nth-child(1) > .border-div")
    BTN_NEXT = (By.ID, "btn-create-listing-transferType")
    DROPDOWN_QUANT = (By.ID, "input-dropdown-quantity-select")
    DROPDOWN_OG_PURCHASE = (By.CSS_SELECTOR, "#input-dropdown-ticket-wallet-primary-vendor > .absolute-full")
    DROPDOWN_LOC = (By.ID, "input-dropdown-ticket-wallet-ga-section")
    INPUT_PRICE = (By.ID, "input-number-create-listing-price-per")
    RADIO_VALUE = (By.CSS_SELECTOR, ".space-y-3 > .flex:nth-child(1)")
    BTN_ADD_PAY = (By.CLASS_NAME, "block w-full sm:w-auto rounded-lg border-2 border-primary border-solid px-6 py-3 relative flex justify-center items-center svelte-1cvyoxz")
    INPUT_CARD_NUM = (By.ID, "Field-numberInput")
    BTN_NEXT_ADD_PAY = (By.ID, "btn-create-listing-creditCardInformation")
    BTN_NEXT_CREATE_LIST = (By.ID,"btn-create-listing-ticketListing")
    BTN_POST = (By.ID, "btn-create-listing-listingReview")
    WALLET_WRAPPER = (By.ID, "ticket-wallet-wrapper")


    def __init__(self, driver):
        self.driver = driver
    
    def create_user(self, name, mail):

        WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(self.INPUT_USR)
        )
        user_input = self.driver.find_element(*self.INPUT_USR)
        user_input.send_keys(name)

        mail_input = self.driver.find_element(By.ID, self.INPUT_MAIL)
        mail_input.send_keys(mail)

        #Accepting Terms of Service
        check_box = self.driver.find_element(By.CSS_SELECTOR, self.CHECKBOX)
        check_box.click()

        submit_button = self.driver.find_element(By.ID, self.BTN_SUBMIT)
        submit_button.click()

        #Skipping profile pic selection
        WebDriverWait(self.driver, 45).until(
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

        for i, performer in enumerate(performers):
            try:
                self.driver.find_element(By.ID, "performer-result-" + str(i)).click()
                self.driver.implicitly_wait(2)

                # Check if there is a nested element with ID "search-event-result-0"
                try:
                    nested_element = self.driver.find_element(By.ID, "search-event-result-0")
                    perfs_with_event.append(nested_element)
                    #go back
                    self.driver.find_element(By.CLASS_NAME, "text-primary font-medium").click()
                except NoSuchElementException:
                    pass  # No nested element found, continue with the next performer
            except StaleElementReferenceException:
                print(f"Element at index {i} became stale. Skipping.")
            continue

            
        if perfs_with_event:        
        #select the first performer found that has registered an event
            perfs_with_event[0].click()
            #  WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(self.BTN_EVENT)
            # )    

            # event = self.driver.find_element(*self.BTN_EVENT)
            # event.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.BTN_EVENT_SELL)
            ) 

            sell_btn = self.driver.find_element(*self.BTN_EVENT_SELL)
            sell_btn.click()
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located(self.BTN_DIGITAL_TRANSF)
            # )

            digital_transfer_btn = self.driver.find_element(*self.
            BTN_DIGITAL_TRANSF)
            digital_transfer_btn.click()
           
            
            next_btn = self.driver.find_element(*self.BTN_NEXT)
            next_btn.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.DROPDOWN_QUANT)
            )

            quantity_dropdown = self.driver.find_element(*self.DROPDOWN_QUANT)
            quantity_dropdown.click()
            self.driver.implicitly_wait(2)
            quantity_amount_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            quantity_amount_1.click()
            self.driver.implicitly_wait(2)

            ready_btn = self.driver.find_element(By.ID, "btn-selector-ready")
            ready_btn.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.DROPDOWN_OG_PURCHASE)
            )
           
            og_purchase = self.driver.find_element(*self.DROPDOWN_OG_PURCHASE)
            self.driver.execute_script("arguments[0].scrollIntoView();", og_purchase)
            og_purchase.click()

            og_purchase_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            og_purchase_1.click()
            self.driver.implicitly_wait(2)

            ticket_info = self.driver.find_element(By.ID, "btn-selector-general-admission")
            ticket_info.click()
            self.driver.implicitly_wait(2)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.DROPDOWN_LOC)
            )

            ticket_loc_dropdown = self.driver.find_element(*self.DROPDOWN_LOC)
            ticket_loc_dropdown.click()
            self.driver.implicitly_wait(2)

            ticket_loc_selection =  self.driver.find_element(By.ID, "input-dropdown-option-7")
            ticket_loc_selection.click()
            self.driver.implicitly_wait(2)

            next_btn = self.driver.find_element(By.ID, "btn-create-listing-mediumSpecificInfo")
            next_btn.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.INPUT_PRICE)
            )

            price_input = self.driver.find_element(*self.INPUT_PRICE)
            price_input.send_keys("12")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.RADIO_VALUE)
            )


            face_value_radio = self.driver.find_element(*self.RADIO_VALUE)
            self.driver.execute_script("arguments[0].scrollIntoView();", face_value_radio)
            face_value_radio.click()

            next_btn = self.driver.find_element(By.ID, "btn-create-listing-ticketPricing")
            next_btn.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.BTN_ADD_PAY)
            )            
                     
            #TODO: Change locator for payment element
            add_payment = self.driver.find_element(*self.BTN_ADD_PAY)
            add_payment.click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.INPUT_CARD_NUM)
            ) 

            card_number_input = self.driver.find_element(*self.INPUT_CARD_NUM)
            card_number_input.send_keys("4242424242424242")

            expiration_number_input = self.driver.find_element(By.ID, "Field-expiryInput")
            month = datetime.today().month
            year = datetime.today().year + 1        
            expiration_number_input.send_keys(month + year)

            cvc_input = self.driver.find_element(By.ID, "Field-cvcInput")
            cvc_input.send_keys("123")

            name_input = self.driver.find_element(By.ID, "Field-nameInput")
            name_input.send_keys(User.__name__)

            address_input = self.driver.find_element(By.CLASS_NAME, "Field-addressLine1Input")
            address_input.send_keys("some_address")

            postal_code_input = self.driver.find_element(By.ID, "Field-postalCodeInput")
            postal_code_input.send_keys("1832")

            city_input = self.driver.find_element(By.ID, "Field-localityInput")
            city_input.send_keys("lomas")

            province_dropdown = self.driver.find_element(By.ID, "Field-administrativeAreaInput")
            province_dropdown.click()
            provinces_select = self.driver.find_elements(By.TAG_NAME, "option")
            provinces_select[0].click()


            submit_btn = self.driver.find_element(By.ID, "btn-submit")
            submit_btn.click()
            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(self.BTN_NEXT_ADD_PAY)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_ADD_PAY)
            next_btn.click()
            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(self.BTN_NEXT_CREATE_LIST)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_CREATE_LIST)
            next_btn.click()

            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(self.BTN_POST)
            )
            post_btn = self.driver.find_element(*self.BTN_POST)
            post_btn.click()

        else:
            raise NoPerformersWithEventsError("No performers with events found.")

class NoPerformersWithEventsError(Exception):
    pass


        
