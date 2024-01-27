import time

from django.test import TestCase, override_settings, TransactionTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dashboard.models import Robot


class ModelTestCase(TestCase):
    def test_robot_model_created_successfully(self):
        robot = Robot(name="Robot 1", motor_type="DC")

        self.assertEqual(robot.name, "Robot 1")
        self.assertEqual(robot.motor_type, "DC")

    def test_robot_model_created_with_null_name_should_fail(self):
        pass

    def test_robot_run_model_created_successfully(self):
        pass

    def test_robot_run_distance_max_value_limit(self):
        pass


class ViewsTestCase(TestCase):
    def test_login_user(self):
        pass

    def test_register_user(self):
        pass

    def test_logout_user(self):
        pass

    def test_show_robot_run(self):
        pass

    # @override_settings(LOGIN_URL='')
    def test_register_robot_get_method(self):
        url = reverse('register-robot')

        # Users.

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_robot.html')

    # TODO is this integration test?
    def test_register_robot_post_method(self):
        url = reverse('register-robot')
        data = {'name': 'Robot 3', 'motor_type': 'servo'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Robot.objects.count(), 1)

        created_robot = Robot.objects.first()

        self.assertEqual(created_robot.name, 'Robot 3')
        self.assertEqual(created_robot.motor_type, 'servo')
        self.assertTemplateUsed(response, 'register_robot.html')

    def test_show_robot_detail_post_method(self):
        pass


class ViewsIntegrationTestCase(TransactionTestCase):
    def register_robot(self):
        name = 'Robot integration test'

        response = self.client.post(reverse('register'),
                                    {'name': name, 'motor_type': 'motor integration test'})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Robot.objects.filter(name=name).count(), 1)

class EndToEndTestCase(TestCase):
    def test_login_url_has_text(self):
        selenium_webdriver = webdriver.Chrome()
        selenium_webdriver.get("http://127.0.0.1:8000/")

        assert "Login" in selenium_webdriver.page_source

    def test_login_button_exists(self):
        selenium_webdriver = webdriver.Chrome()
        selenium_webdriver.get("http://127.0.0.1:8000/")

        # login_inputs = selenium_webdriver.find_element(By.ID, "login-input")

        login_button = selenium_webdriver.find_element(By.ID, "login-button")

        # click on the button
        login_button.send_keys(Keys.RETURN)

        # assert "Robot run" in selenium_webdriver.page_source
