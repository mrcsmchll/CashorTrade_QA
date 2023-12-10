import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.home import Home
from pages.login import Login

class TestHome:
    @pytest.fixture(scope="function")
    def setup(self):
        driver = webdriver.Chrome()
        driver.get(Home.URL)
        yield driver
        driver.quit()
    
    def test_desktop_login_navigation(self, setup):
        driver = setup
        home_page = Home(driver)
        home_page.click_login_desktop()
        # Explicitly wait for the URL to update
        WebDriverWait(driver, 10).until(
            EC.url_contains("register")
        )
        assert "register" in driver.current_url.lower()

    def test_mobile_login_navigation(self, setup):
        driver = setup
        driver.set_window_size(375, 667)

        home_page = Home(driver)
        home_page.click_login_mobile()
        phone_input = Login.INPUT_PHONE
         # Explicitly wait for the URL to update
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Home.OVERLAY_LOC)
        )

        assert driver.find_element(By.ID, phone_input)     