from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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
    BTN_ADD_PAY = (By.CSS_SELECTOR, "#ticket-wallet-wrapper > div > div.relative.flex-1.overflow-y-scroll.scrollbar-hide.px-6.pb-12.z-1 > div.mb-6 > div > div.mb-8.space-y-3 > div.space-y-2 > button")
    IFRAME_CARD = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div[3]/div[1]/div/div[1]/div[2]/form/div[1]/div[1]/div/iframe")
    IFRAME_BILLING_ADDRESS = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div[3]/div[1]/div/div[1]/div[2]/form/div[1]/div[2]/div/iframe[1]")
    INPUT_CARD_NUM = (By.CSS_SELECTOR, "#card > div > div > form > div > div.p-Grid.p-CardForm > div.p-GridCell.p-GridCell--12.p-GridCell--md6 > div > div > div")
    BTN_NEXT_ADD_PAY = (By.ID, "btn-create-listing-creditCardInformation")
    BTN_NEXT_CREATE_LIST = (By.ID,"btn-create-listing-ticketListing")
    BTN_POST = (By.ID, "btn-create-listing-listingReview")
    WALLET_WRAPPER = (By.ID, "ticket-wallet-wrapper")
    PERFORMERS_WRAPPER = (By.CLASS_NAME, "space-y-3 transform translate-y-0 hoist-undefined svelte-1xzbzxf")
    BTN_FRST_PERF = (By.ID, "performer-result-0")

    CALL_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
    
    def create_user(self, name, mail):

        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
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
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.url_contains("profile-picture")
        )

        skip_pic = self.driver.find_element(By.ID, self.BTN_SKIP_PIC)
        skip_pic.click()        

    def skip_walkthrough(self):
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.visibility_of_element_located(self.BTN_SKIP_WLK)
        )
        self.driver.find_element(*self.BTN_SKIP_WLK).click()

    def sell_ticket(self, user):
        self.driver.find_element(By.ID, self.BTN_SELL).click()
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.presence_of_element_located(self.BTN_FRST_PERF)
        )    

        # performers = self.driver.find_elements(*self.PERFORMERS_WRAPPER)
        # perfs_with_event = []
        first_performer = self.driver.find_element(*self.BTN_FRST_PERF)
        first_performer.click()
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.visibility_of_element_located(self.BTN_EVENT)
        )
        # for i, performer in enumerate(performers):
        #     try:
                
        #         first_performer = self.driver.find_element(*self.BTN_FRST_PERF).click()
        #         WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
        #             EC.visibility_of_element_located(first_performer)
        #         )
                
                

        #         # Check if there is a nested element with ID "search-event-result-0"
        #         try:
                    
        #             WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
        #                 EC.visibility_of_element_located(self.BTN_EVENT)
        #             )

        #             nested_element = self.driver.find_element(*self.BTN_EVENT)

        #             WebDriverWait(self.driver, self.CALL_TIMEOUT)
                    
        #             perfs_with_event.append(nested_element)
        #             #go back
        #             self.driver.find_element(By.CLASS_NAME, "flex items-center").click()
        #         except NoSuchElementException:
        #             pass  # No nested element found, continue with the next performer
        #     except StaleElementReferenceException:
        #         print(f"Element at index {i} became stale. Skipping.")
        #     continue

            
        if first_performer is not None:        
        #select the first performer found that has registered an event
            # first_performer.click()
            #  WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            #     EC.visibility_of_element_located(self.BTN_EVENT)
            # )    

            event = self.driver.find_element(*self.BTN_EVENT)
            event.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.BTN_EVENT_SELL)
            ) 

            sell_btn = self.driver.find_element(*self.BTN_EVENT_SELL)
            sell_btn.click()
            # WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            #     EC.visibility_of_element_located(self.BTN_DIGITAL_TRANSF)
            # )

            digital_transfer_btn = self.driver.find_element(*self.
            BTN_DIGITAL_TRANSF)
            digital_transfer_btn.click()
           
            
            next_btn = self.driver.find_element(*self.BTN_NEXT)
            next_btn.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DROPDOWN_QUANT)
            )

            quantity_dropdown = self.driver.find_element(*self.DROPDOWN_QUANT)
            quantity_dropdown.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT)

            quantity_amount_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            quantity_amount_1.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT)

            ready_btn = self.driver.find_element(By.ID, "btn-selector-ready")
            ready_btn.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DROPDOWN_OG_PURCHASE)
            )
           
            og_purchase = self.driver.find_element(*self.DROPDOWN_OG_PURCHASE)
            self.driver.execute_script("arguments[0].scrollIntoView();", og_purchase)
            og_purchase.click()

            og_purchase_1 = self.driver.find_element(By.ID, "input-dropdown-option-0")
            og_purchase_1.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT)

            ticket_info = self.driver.find_element(By.ID, "btn-selector-general-admission")
            ticket_info.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DROPDOWN_LOC)
            )

            ticket_loc_dropdown = self.driver.find_element(*self.DROPDOWN_LOC)
            ticket_loc_dropdown.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT)

            ticket_loc_selection =  self.driver.find_element(By.ID, "input-dropdown-option-7")
            ticket_loc_selection.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT)

            next_btn = self.driver.find_element(By.ID, "btn-create-listing-mediumSpecificInfo")
            next_btn.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.INPUT_PRICE)
            )

            price_input = self.driver.find_element(*self.INPUT_PRICE)
            price_input.send_keys("12")
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.RADIO_VALUE)
            )


            face_value_radio = self.driver.find_element(*self.RADIO_VALUE)
            self.driver.execute_script("arguments[0].scrollIntoView();", face_value_radio)
            face_value_radio.click()

            next_btn = self.driver.find_element(By.ID, "btn-create-listing-ticketPricing")
            next_btn.click()

            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_ADD_PAY)
            )            
                     
            add_payment = self.driver.find_element(*self.BTN_ADD_PAY)
            add_payment.click()

            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(locator=[By.CLASS_NAME, "__PrivateStripeElement"])
            )

            #Attempt at working with Stripe's iframes    
            card_frame_element = self.driver.find_element(By.ID, "payment-element")
            iframe_container = card_frame_element.find_element(By.CLASS_NAME, "__PrivateStripeElement")
            iframe = iframe_container.find_element(By.XPATH, '//*[@id="payment-element"]/div/iframe')
            self.driver.switch_to.frame(iframe)
            
            is_stale = WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.staleness_of(iframe)
            )
            
            i = 0
            while is_stale and i < 20:
                is_stale = WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                    EC.staleness_of(iframe)
                )
                WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                    EC.presence_of_element_located(locator=[By.XPATH, "//*[@id='Field-numberInput']"])
                )
                
                i += 1
                        
                
           
            
            card_number_input = self.driver.find_element(By.XPATH, "//*[@id='Field-numberInput']")          
            card_number_input.send_keys("4242424242424242")
            

            month = datetime.today().month
            year = datetime.today().year + 1
            expiration_number_input = self.driver.find_element(By.ID,"Field-expiryInput")
            expiration_number_input.send_keys(str(month) + str(year)[-2:])

            cvc_input = self.driver.find_element(By.ID, "Field-cvcInput")
            cvc_input.send_keys("123")
            
            #Switching Stripe's iframes
            self.driver.switch_to.default_content()
            address_frame_element = self.driver.find_element(By.ID, "billing-address")
            iframe_container = address_frame_element.find_element(By.CLASS_NAME, "__PrivateStripeElement")
            iframe = iframe_container.find_element(By.TAG_NAME, "iframe")
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.frame_to_be_available_and_switch_to_it(iframe)
            )
            self.driver.switch_to.frame(iframe)

            name_input = self.driver.find_element(By.ID, "Field-nameInput")
            name_input.send_keys(user.name)
            
            address_input = self.driver.find_element(By.CLASS_NAME, "Field-addressLine1Input")
            self.driver.execute_script("arguments[0].scrollIntoView();", address_input)
            address_input.send_keys("some_address")

            postal_code_input = self.driver.find_element(By.ID, "Field-postalCodeInput")
            postal_code_input.send_keys("1832")

            city_input = self.driver.find_element(By.ID, "Field-localityInput")
            city_input.send_keys("lomas")

            province_dropdown = self.driver.find_element(By.ID, "Field-administrativeAreaInput")
            province_dropdown.click()
            provinces_select = self.driver.find_elements(By.TAG_NAME, "option")
            provinces_select[0].click()

            #Back to main content
            self.driver.switch_to.default_content()

            submit_btn = self.driver.find_element(By.ID, "btn-submit")
            submit_btn.click()
            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.BTN_NEXT_ADD_PAY)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_ADD_PAY)
            next_btn.click()
            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.BTN_NEXT_CREATE_LIST)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_CREATE_LIST)
            next_btn.click()

            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.BTN_POST)
            )
            post_btn = self.driver.find_element(*self.BTN_POST)
            post_btn.click()

        else:
            raise NoPerformersWithEventsError("No performers with events found.")

class NoPerformersWithEventsError(Exception):
    pass


        
