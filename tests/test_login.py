import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.db import Database
from utils.utils import Utils
from utils.user import User
from pages.home import Home
from pages.login import Login
from pages.auth import Auth
from pages.account import Account

class TestLogin:
    CALL_TIMEOUT = 10

    @pytest.fixture(scope="function")
    def setup(self):
        self.user = User(Utils.generate_name(),Utils.random_phone_number())
        #saving on txt for easy access
        Utils.user_save(self.user)
        # Initialize the database
        db = Database()
        db.insert_user(self.user.name, self.user.mail, self.user.phone)

        #As of Chrome 95, on MacOS and Windows, "--disable-site-isolation-trials" remains a required flag in order to disable web security
        options = Options()
        options.add_argument("--disable-site-isolation-trials")
        options.add_argument("--disable-web-security")

        driver = webdriver.Chrome(options)
        driver.get(Home.URL)
        yield driver
        driver.quit()
        

    def test_login(self, setup):
        driver = setup

        home_page = Home(driver)
        home_page.click_login_desktop()
        WebDriverWait(driver, self.CALL_TIMEOUT).until(
            EC.url_contains("register")
        )
        assert "register" in driver.current_url.lower()

        login_page = Login(driver)
        login_page.login_with_phone_num(self.user.phone)        
        WebDriverWait(driver, self.CALL_TIMEOUT).until(
            EC.url_contains("verify")
        )
        assert "verify" in driver.current_url.lower()

        auth_page = Auth(driver)
        auth_page.verify_phone()
        WebDriverWait(driver, self.CALL_TIMEOUT).until(
            EC.url_contains("account")
        )
        assert "account" in driver.current_url.lower()

        acc_page = Account(driver)
        acc_page.create_user(self.user.name, self.user.mail)

        assert "profile" in driver.current_url.lower()

        acc_page.skip_walkthrough()

        acc_page.sell_ticket(self.user.name)
        
            


    
    
