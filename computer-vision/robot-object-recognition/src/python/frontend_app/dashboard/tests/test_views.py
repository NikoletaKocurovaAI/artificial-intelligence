from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.forms import RegistrationForm
from dashboard.models import Robot


class ViewsUnitTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

    def test_login_user(self) -> None:
        def test_logout_user(self):
            # Make a GET request to the logout URL
            response = self.client.get(reverse("logout"))

            # Check that the response is a redirect to the login page
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse("custom-login"))

            # Check that the user is logged out
            user = authenticate(username=self.username, password=self.password)
            self.assertIsNone(user)

            # Make another request to ensure the user is no longer authenticated
            response = self.client.get("/")  # Change the URL as needed
            self.assertEqual(
                response.status_code, 200
            )  # Assuming the home page returns 200 status code
            self.assertNotIn(
                "_auth_user_id", self.client.session
            )  # Check that the user is not in the session

        def tearDown(self):
            # Clean up - log out the user
            logout(self.client)

    def test_register_user_renders_register_form(self):
        # Make a GET request to the register URL
        response = self.client.get(reverse("register"))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, "register.html")

        # Check that the RegistrationForm instance is passed to the template context
        self.assertIsInstance(response.context["form"], RegistrationForm)

    def test_register_user_submits_valid_registration_data(self) -> None:
        pass
        # # Prepare valid registration data
        # valid_data = {
        #     'username': 'testuser',
        #     'password1': 'testpassword',
        #     'password2': 'testpassword',
        # }
        #
        # # Make a POST request to the register URL with valid data
        # response = self.client.post(reverse('register'), valid_data, follow=True)
        #
        # # Check that the user is redirected to the login page
        # self.assertRedirects(response, reverse('custom-login'))
        #
        # # Check that the user is created in the database
        # self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_user_submits_invalid_registration_data(self) -> None:
        pass
        # # Prepare invalid registration data
        # invalid_data = {
        #     'username': '',  # Invalid: username is required
        #     'password1': 'testpassword',
        #     'password2': 'testpassword',
        # }
        #
        # # Make a POST request to the register URL with invalid data
        # response = self.client.post(reverse('register'), invalid_data, follow=True)
        #
        # # Check that the response status code is 200
        # self.assertEqual(response.status_code, 200)
        #
        # # Check that the correct template is used
        # self.assertTemplateUsed(response, 'register.html')
        #
        # # Check that the RegistrationForm instance with errors is passed to the template context
        # self.assertIsInstance(response.context['form'], RegistrationForm)
        # self.assertTrue(response.context['form'].errors)

    def test_register_user(self):
        pass

    def test_logout_user(self):
        pass

    def test_show_robot_run(self):
        pass

    def test_register_robot_get_method(self):
        url = reverse("register-robot")

        # Users.

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register_robot.html")

    # TODO is this integration test?
    def test_register_robot_post_method(self):
        url = reverse("register-robot")
        data = {"name": "Robot 3", "motor_type": "servo"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Robot.objects.count(), 1)

        created_robot = Robot.objects.first()

        self.assertEqual(created_robot.name, "Robot 3")
        self.assertEqual(created_robot.motor_type, "servo")
        self.assertTemplateUsed(response, "register_robot.html")

    def test_show_robot_detail_post_method(self):
        pass
