from django.test import TestCase
from django.urls import reverse

from dashboard.models import Robot


class ViewsUnitTestCase(TestCase):
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
