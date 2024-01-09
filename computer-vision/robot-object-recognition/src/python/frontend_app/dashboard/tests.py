from django.test import TestCase
from dashboard.models import Robot


class ModelTestCase(TestCase):
    def test_model_creation(self):
        robot = Robot(name="Robot 1", motor_type="DC")

        self.assertEqual(robot.name, "Robot 1")
        self.assertEqual(robot.motor_type, "DC")
