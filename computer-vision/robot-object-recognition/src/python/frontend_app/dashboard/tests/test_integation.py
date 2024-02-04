from django.test import TestCase

from dashboard.models import Robot
from django.urls import reverse


class ViewsIntegrationTestCase(TestCase):
    # TODO this test fails in pipeline due to missing DB credentials
    def register_robot(self) -> None:
        name = "Robot integration test"

        response = self.client.post(
            reverse("register"), {"name": name, "motor_type": "motor integration test"}
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Robot.objects.filter(name=name).count(), 1)
