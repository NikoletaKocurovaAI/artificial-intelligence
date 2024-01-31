from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from django.test import TestCase


class EndToEndTestCase(TestCase):
    def test_login_url_has_text(self):
        selenium_webdriver = webdriver.Chrome()
        selenium_webdriver.get("http://127.0.0.1:8000/")

        assert "Login" in selenium_webdriver.page_source

    def test_login_button_redirects_to_robot_run(self):
        selenium_webdriver = webdriver.Chrome()
        selenium_webdriver.get("http://127.0.0.1:8000/")

        username_input = selenium_webdriver.find_element(By.ID, "username")
        username_input.send_keys("admin")

        password_input = selenium_webdriver.find_element(By.ID, "password")
        password_input.send_keys("admin")

        login_button = selenium_webdriver.find_element(By.ID, "login-button")
        login_button.send_keys(Keys.RETURN)

        assert "Robot run" in selenium_webdriver.page_source
