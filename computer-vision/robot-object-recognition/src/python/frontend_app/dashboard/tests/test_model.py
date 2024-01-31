import datetime
from django.test import TestCase, override_settings, TransactionTestCase

from dashboard.models import Robot, RobotRun


class ModelUnitTestCase(TestCase):
    def setUp(self) -> None:
        self.robot1 = Robot.objects.create(
            name="Robot Test1", motor_type="motor type test"
        )
        self.robot2 = Robot.objects.create(
            name="Robot Test2", motor_type="motor type test"
        )

        self.robot_run1 = RobotRun.objects.create(
            robot_id=1,
            started=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            finished=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="completed",
            distance=7,
        )

        self.robot_run2 = RobotRun.objects.create(
            robot_id=2,
            started=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            finished=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="error",
            distance=7,
        )

        self.robot_run3 = RobotRun.objects.create(
            robot_id=3,
            started=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            finished=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            status="error",
            distance=7,
        )

    def test_robot_model_created_successfully(self) -> None:
        robot = Robot(name=self.robot1.name, motor_type=self.robot1.motor_type)

        self.assertEqual(robot.name, self.robot1.name)
        self.assertEqual(robot.motor_type, self.robot1.motor_type)

    def test_get_robot_by_id(self) -> None:
        retrieved_robot = Robot.get_by_id(Robot(), self.robot1.id)

        self.assertEqual(retrieved_robot.get("name"), "Robot Test1")

    def test_robot_run_model_created_successfully(self) -> None:
        robot_run = RobotRun(
            robot_id=self.robot_run1.robot_id,
            started=self.robot_run1.started,
            finished=self.robot_run1.finished,
            status=self.robot_run1.status,
            distance=self.robot_run1.distance,
        )

        self.assertEqual(robot_run.robot_id, self.robot_run1.robot_id)
        self.assertEqual(robot_run.started, self.robot_run1.started)
        self.assertEqual(robot_run.finished, self.robot_run1.finished)
        self.assertEqual(robot_run.status, self.robot_run1.status)
        self.assertEqual(robot_run.distance, self.robot_run1.distance)

    def test_add_robot_name_to_robot_run(self) -> None:
        robot_runs = RobotRun.objects.none()

        robot_runs = (
            robot_runs
            | RobotRun.objects.filter(robot_id=self.robot_run1.robot_id).values()
        )
        robot_runs = (
            robot_runs
            | RobotRun.objects.filter(robot_id=self.robot_run2.robot_id).values()
        )
        robot_runs = (
            robot_runs
            | RobotRun.objects.filter(robot_id=self.robot_run3.robot_id).values()
        )

        result = RobotRun.add_robot_name(list(robot_runs))

        self.assertEqual(result[0].get("robot_name"), self.robot1.name)
        self.assertEqual(result[1].get("robot_name"), self.robot2.name)
        self.assertEqual(result[2].get("robot_name"), "")

    def test_get_filtered_robot_runs(self) -> None:
        result_all = RobotRun.get_filtered_robot_runs(status="all")
        result_error = RobotRun.get_filtered_robot_runs(status="error")
        result_running = RobotRun.get_filtered_robot_runs(status="running")
        result_completed = RobotRun.get_filtered_robot_runs(status="completed")

        self.assertEqual(len(result_all), 3)
        self.assertEqual(len(result_error), 2)
        self.assertEqual(len(result_running), 0)
        self.assertEqual(len(result_completed), 1)

    def test_get_robots_runs_statuses(self) -> None:
        result = RobotRun.get_robots_runs_statuses()

        self.assertEqual(result[0].get("status"), "all")
        self.assertEqual(result[1].get("status"), "completed")
        self.assertEqual(result[2].get("status"), "error")
