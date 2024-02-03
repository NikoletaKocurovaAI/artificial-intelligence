from django.db.models import Model, DateTimeField, TextField, IntegerField, CharField
from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MaxValueValidator
from typing import List, Dict, Any


"""
    MVC pattern (Model-View-Controller)
    
    Django's MTV:
    Model - Data from database
    Template - Data presentation
    View - Business logic
"""


class Robot(Model):
    name = CharField(max_length=128, null=False, blank=False, default="", unique=True)
    motor_type = CharField(max_length=128, null=False, blank=False, default="")
    next_run = DateTimeField(auto_now_add=False, null=True)

    def get_by_id(self, id: int) -> Dict[str, Any]:
        """
        This method is called by the show_robot_detail view.

        It gets the robot by its ID and returns dictionary, that is used in the robot_detail.html.

        :param int id: Robot ID
        :return: Dict[str, Any] Robot object with attributes id, name, motor_type, next_run
        :raises
        """

        robot: Dict[str, Any] = Robot.objects.filter(id=id).values().first()

        return robot

    def validate_name(self):
        """
        This ..

        :param request:
        :return:
        :raises
        """

        # TODO validate method replace with clean()
        pass


class RobotRun(Model):
    robot_id = IntegerField(null=False, blank=False, default=0)
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(
        null=False,
        blank=False,
        default=0,
        validators=[MinValueValidator(5), MaxValueValidator(20)],
    )

    class Meta:
        ordering = ["-distance"]

    @staticmethod
    def add_robot_name(robots_runs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        This method is called by the show_robot_run view.

        To all robot runs, it gets robot names and adds them to the robot runs object.

        Returned values are used in the robot_run.html.

        :param List[Dict[str, Any] robots_runs: The list of robot run objects, that should be enriched by the robot
        names
        :return: List[Dict[str, Any]] Robot run objects enriched by the robot names with attributes id, robot_id,
        started, finished, status, distance, robot_name
        :raises
        """

        for robot_run in robots_runs:
            try:
                robot: Robot = Robot.objects.get(id=robot_run["robot_id"])
                robot_run["robot_name"] = robot.name

            except ObjectDoesNotExist:
                robot_run["robot_name"] = ""

        return robots_runs

    @staticmethod
    def get_filtered_robot_runs(status: str) -> List[Dict[str, Any]]:
        """
        This method is called by the show_robot_run view.

        Status has either value "all", in this case no filter is applied. Or it contains the status value, that is used
        to filter results from the robot run table and show these filtered results in the table on robot-run page.

        Returned values are used in the robot_run.html.

        :param str status: The status passed from the view, to filter results in the table on robot-run page.
        :return: List[Dict[str, Any]] Robot run objects filtered or not filtered by status with attributes id, robot_id,
        started, finished, status, distance
        :raises
        """

        if status == "all":
            robots_runs: List[Dict[str, Any]] = list(RobotRun.objects.filter().values())
        else:
            robots_runs: List[Dict[str, Any]] = list(
                RobotRun.objects.filter(status=status).values()
            )

        return robots_runs

    @staticmethod
    def get_robots_runs_statuses() -> List[Dict[str, str]]:
        """
        This method is called by the show_robot_run view.

        It gets sorted statuses from the robot run table, which are not unique. The unique values are stored in the
        variable distinct_robots_runs_statuses. It appends "all" option in the variable
        postprocessed_robots_runs_statuses on the first index meaning, that applied "all" filter will be shown as the
        first option in the UI. Then the rest of statuses is appended to this variable.

        Returned values are used in the robot_run.html.

        :return: List[Dict[str, str]]: The list of statuses, that are used on the robot-run page to filter table
        results.
        :raises
        """

        statuses: QuerySet[List[str]] = (
            RobotRun.objects.order_by("status")
            .values_list("status", flat=True)
            .distinct()
        )

        postprocessed_robots_runs_statuses: List[Dict[str, str]] = list()

        postprocessed_robots_runs_statuses.append({"status": "all"})

        for item in statuses:
            postprocessed_robots_runs_statuses.append({"status": item})

        return postprocessed_robots_runs_statuses
