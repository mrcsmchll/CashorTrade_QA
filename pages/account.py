from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from config.card_info import Card

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
    BTN_READY = (By.ID, "btn-selector-ready")
    BTN_GRAL_ADM = (By.ID, "btn-selector-general-admission")
    BTN_ADD_TICKET = (By.ID, "btn-create-listing-mediumSpecificInfo")
    BTN_CREATE_LIST = (By.ID, "btn-create-listing-ticketPricing")
    INPUT_DROPDOWN = (By.ID, "input-dropdown-option-0")
    DROPDOWN_TICKET_LOC = (By.ID, "input-dropdown-option-7")
    DROPDOWN_QUANT = (By.ID, "input-dropdown-quantity-select")
    DROPDOWN_OG_PURCHASE = (By.CSS_SELECTOR, "#input-dropdown-ticket-wallet-primary-vendor > .absolute-full")
    DROPDOWN_LOC = (By.ID, "input-dropdown-ticket-wallet-ga-section")
    INPUT_PRICE = (By.ID, "input-number-create-listing-price-per")
    RADIO_VALUE = (By.CSS_SELECTOR, ".space-y-3 > .flex:nth-child(1)")
    BTN_ADD_PAY = (By.CSS_SELECTOR, "#ticket-wallet-wrapper > div > div.relative.flex-1.overflow-y-scroll.scrollbar-hide.px-6.pb-12.z-1 > div.mb-6 > div > div.mb-8.space-y-3 > div.space-y-2 > button")
    DIV_STRIPE_CARD = (By.CLASS_NAME, "__PrivateStripeElement")
    CARD_FRAME = (By.ID, "payment-element")
    IFRAME_CONTAINER = (By.XPATH, '//*[@id="payment-element"]/div/iframe')
    IFRAME_BILLING_ADDRESS = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div[3]/div[1]/div/div[1]/div[2]/form/div[1]/div[2]/div/iframe[1]")
    INPUT_CARD_NUM = (By.XPATH, "//*[@id='Field-numberInput']")
    INPUT_EXPIRATION_CARD = (By.ID,"Field-expiryInput")
    INPUT_CVC = (By.ID, "Field-cvcInput")
    INPUT_BILLING_ADDSS = (By.ID, "billing-address")
    TAG_IFRAME = (By.TAG_NAME, "iframe")
    INPUT_NAME = (By.XPATH, '//*[@id="Field-nameInput"]')
    INPUT_ADDRESS = (By.XPATH,'//*[@id="Field-addressLine1Input"]')
    INPUT_POSTAL_CODE = (By.XPATH, '//*[@id="Field-postalCodeInput"]')
    INPUT_LOCALITY = (By.XPATH, '//*[@id="Field-localityInput"]')
    FORM_PAYMENT = (By.XPATH, '//*[@id="payment-form"]')
    BTN_FORM_SUBMIT = (By.XPATH, '//*[@id="btn-submit"]')
    DROPDOWN_PROV = (By.XPATH, '//*[@id="Field-administrativeAreaInput"]')
    BTN_NEXT_ADD_PAY = (By.ID, "btn-create-listing-creditCardInformation")
    BTN_NEXT_CREATE_LIST = (By.ID,"btn-create-listing-ticketListing")
    BTN_POST = (By.ID, "btn-create-listing-listingReview")
    TICKET_WALLET_WRAPPER = (By.XPATH, '//*[@id="ticket-wallet-wrapper"]/div/div[4]')
    PERFORMERS_WRAPPER = (By.CLASS_NAME, "space-y-3 transform translate-y-0 hoist-undefined svelte-1xzbzxf")
    BTN_FRST_PERF = (By.ID, "performer-result-0")

    CALL_TIMEOUT = 10
    IFRAME_REPEAT = 20

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

    def sell_ticket(self, name):
        self.driver.find_element(By.ID, self.BTN_SELL).click()
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.presence_of_element_located(self.BTN_FRST_PERF)
        )    

      
        first_performer = self.driver.find_element(*self.BTN_FRST_PERF)
        first_performer.click()
        WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
            EC.visibility_of_element_located(self.BTN_EVENT)
        )
       
        if first_performer is not None:        

            event = self.driver.find_element(*self.BTN_EVENT)
            event.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.BTN_EVENT_SELL)
            ) 

            sell_btn = self.driver.find_element(*self.BTN_EVENT_SELL)
            sell_btn.click()

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
            
            quantity_amount_1 = self.driver.find_element(*self.INPUT_DROPDOWN)
            quantity_amount_1.click()

            ready_btn = self.driver.find_element(*self.BTN_READY)
            ready_btn.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DROPDOWN_OG_PURCHASE)
            )
           
            og_purchase = self.driver.find_element(*self.DROPDOWN_OG_PURCHASE)
            self.driver.execute_script("arguments[0].scrollIntoView();", og_purchase)
            og_purchase.click()

            og_purchase_1 = self.driver.find_element(*self.INPUT_DROPDOWN)
            og_purchase_1.click()

            ticket_info = self.driver.find_element(*self.BTN_GRAL_ADM)
            ticket_info.click()
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DROPDOWN_LOC)
            )

            ticket_loc_dropdown = self.driver.find_element(*self.DROPDOWN_LOC)
            ticket_loc_dropdown.click()

            ticket_loc_selection =  self.driver.find_element(*self.DROPDOWN_TICKET_LOC)
            ticket_loc_selection.click()

            next_btn = self.driver.find_element(*self.BTN_ADD_TICKET)
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

            next_btn = self.driver.find_element(*self.BTN_CREATE_LIST)
            next_btn.click()

            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_ADD_PAY)
            )            
                     
            add_payment = self.driver.find_element(*self.BTN_ADD_PAY)
            add_payment.click()

            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.visibility_of_element_located(self.DIV_STRIPE_CARD)
            )

            #Attempt at working with Stripe's iframes    
            card_frame_element = self.driver.find_element(*self.CARD_FRAME)
            iframe_container = card_frame_element.find_element(*self.DIV_STRIPE_CARD)
            iframe = iframe_container.find_element(*self.IFRAME_CONTAINER)
            self.driver.switch_to.frame(iframe)
            
            is_stale = WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.staleness_of(iframe)
            )
            
            i = 0
            while is_stale and i < self.IFRAME_REPEAT:
                is_stale = WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                    EC.staleness_of(iframe)
                )
                WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                    EC.presence_of_element_located(self.INPUT_CARD_NUM)
                )
                
                i += 1
                        
                
           
            card = Card()
            card_number_input = self.driver.find_element(*self.INPUT_CARD_NUM)          
            card_number_input.send_keys(card.number)
            
            expiration_number_input = self.driver.find_element(*self.INPUT_EXPIRATION_CARD)
            expiration_number_input.send_keys(card.exp_date)

            cvc_input = self.driver.find_element(*self.INPUT_CVC)
            cvc_input.send_keys(card.cvc)
            
            #Switching Stripe's iframes
            self.driver.switch_to.default_content()
            address_frame_element = self.driver.find_element(*self.INPUT_BILLING_ADDSS)
            iframe_container = address_frame_element.find_element(*self.DIV_STRIPE_CARD)
            iframe = iframe_container.find_element(*self.TAG_IFRAME)
           
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
                    EC.presence_of_element_located(self.INPUT_NAME)
                )
                
                i += 1

            name_input = self.driver.find_element(*self.INPUT_NAME)
            name_input.send_keys(name)
            
            address_input = self.driver.find_element(*self.INPUT_ADDRESS)
            self.driver.execute_script("arguments[0].scrollIntoView();", address_input)
            address_input.send_keys(card.address)

            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.INPUT_POSTAL_CODE)
            )
            postal_code_input = self.driver.find_element(*self.INPUT_POSTAL_CODE)
            postal_code_input.send_keys(card.postal)

            city_input = self.driver.find_element(*self.INPUT_LOCALITY)
            city_input.send_keys(card.city)



            province_dropdown = self.driver.find_element(*self.DROPDOWN_PROV)           
            Select(province_dropdown).select_by_index(1)

            #Back to main content
            self.driver.switch_to.default_content()
            submit_form = self.driver.find_element(*self.FORM_PAYMENT)
            submit_btn = submit_form.find_element(*self.BTN_FORM_SUBMIT)
            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_FORM_SUBMIT)
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
            WebDriverWait(self.driver, self.CALL_TIMEOUT).until(
                EC.invisibility_of_element((self.TICKET_WALLET_WRAPPER))
            )
            submit_btn.click()
            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_NEXT_ADD_PAY)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_ADD_PAY)
            next_btn.click()
            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_NEXT_CREATE_LIST)
            )

            next_btn = self.driver.find_element(*self.BTN_NEXT_CREATE_LIST)
            next_btn.click()

            WebDriverWait(self.driver,self.CALL_TIMEOUT).until(
                EC.element_to_be_clickable(self.BTN_POST)
            )
            post_btn = self.driver.find_element(*self.BTN_POST)
            post_btn.click()

        else:
            raise NoPerformersWithEventsError("No performers with events found.")

class NoPerformersWithEventsError(Exception):
    pass


        
