import datetime

from django.test import TestCase, override_settings, TransactionTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dashboard.models import Robot, RobotRun


class ModelUnitTestCase(TestCase):
    def setUp(self):
        self.robot = Robot.objects.create(name='Robot Test', motor_type="motor type test")

        self.robot_run = RobotRun.objects.create(robot_id=1,
                                                 started=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                 finished=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                 status="completed", distance=7)

    def test_robot_model_created_successfully(self):
        robot = Robot(name=self.robot.name, motor_type=self.robot.motor_type)

        self.assertEqual(robot.name, self.robot.name)
        self.assertEqual(robot.motor_type, self.robot.motor_type)

    def test_get_robot_by_id(self):
        retrieved_robot = Robot.get_by_id(Robot(), self.robot.id)

        self.assertEqual(retrieved_robot.get("name"), "Robot Test")

    def test_robot_run_model_created_successfully(self):
        robot_run = RobotRun(robot_id=self.robot_run.robot_id, started=self.robot_run.started,
                             finished=self.robot_run.finished, status=self.robot_run.status,
                             distance=self.robot_run.distance)

        self.assertEqual(robot_run.robot_id, self.robot_run.robot_id)
        self.assertEqual(robot_run.started, self.robot_run.started)
        self.assertEqual(robot_run.finished, self.robot_run.finished)
        self.assertEqual(robot_run.status, self.robot_run.status)
        self.assertEqual(robot_run.distance, self.robot_run.distance)

    def test_add_robot_name_to_robot_run(self):
        pass

    def test_get_filtered_robot_runs(self):
        pass

    def test_get_robots_runs_statuses(self):
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
