import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.utils import Utils
from pages.login import Login
from pages.auth import Auth
from pages.account import Account

class TestLogin:

    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome()
        driver.get(Login.URL)
        yield driver
        driver.quit()

    def test_login(self, setup):
        driver = setup
        phone = Utils.random_phone_number()
        usr_name = Utils.generate_name()
        usr_mail = usr_name + "@asd.com"
        Utils.user_save(phone, usr_name, usr_mail)

        login_page = Login(driver)
        # Explicitly wait for the URL to update
        WebDriverWait(driver, 10).until(
            EC.url_contains("register")
        )
        login_page.login_with_phone_num(phone)
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("verify")
        )
        auth_page = Auth(driver)
        auth_page.verify_phone()

        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        assert "account" in driver.current_url.lower()

        acc_creator = Account(driver)
        acc_creator.create_user(usr_name, usr_mail)

        assert "profile" in driver.current_url.lower()
    


    
    
