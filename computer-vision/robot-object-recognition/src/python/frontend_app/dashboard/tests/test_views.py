from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.forms import RegistrationForm


# TODO Add test_views to GitHub workflows
class ViewsUnitTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

    def tearDown(self):
        # Clean up - log out the user
        logout(self.client)

    # TODO
    def test_login_user_get_request(self) -> None:
        pass

    # TODO
    def test_login_user_post_request(self) -> None:
        pass

    def test_logout_user(self) -> None:
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

    def test_register_user_renders_register_form(self):
        # Make a GET request to the register URL
        response = self.client.get(reverse("register"))

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the correct template is used
        self.assertTemplateUsed(response, "register.html")

        # Check that the RegistrationForm instance is passed to the template context
        self.assertIsInstance(response.context["form"], RegistrationForm)

    # TODO
    def test_register_user_submits_valid_registration_data(self) -> None:
        pass

    def test_register_user_submits_invalid_registration_data(self) -> None:
        pass

    # TODO
    def test_logout_user(self):
        pass

    # TODO
    def test_show_robot_run(self):
        pass

    # TODO
    def test_register_robot_get_method(self):
        pass

    # TODO
    def test_register_robot_post_method(self):
        pass

    # TODO
    def test_show_robot_detail_post_method(self):
        pass
