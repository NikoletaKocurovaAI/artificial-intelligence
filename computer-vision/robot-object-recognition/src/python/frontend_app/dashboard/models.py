from django.db.models import Model, DateTimeField, TextField, IntegerField, CharField
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator, MaxValueValidator


class Robot(Model):
    name = CharField(max_length=128, null=False, blank=False, default="", unique=True)
    motor_type = CharField(max_length=128, null=False, blank=False, default="")
    next_run = DateTimeField(auto_now_add=False, null=True)

    def get_by_id(self, id):
        robot = Robot.objects.filter(id=id).values()

        robot_payload = []

        for item in robot:
            robot_payload.append({
                "id": item.get("id"),
                "name": item.get("name"),
                "motor_type": item.get("motor_type"),
                "next_run": item.get("next_run")
            })

        return robot_payload[0]

    def validate_name(self):
        # TODO validate method or CharField unique=True
        pass


class RobotRun(Model):
    robot_id = IntegerField(null=False, blank=False, default=0)
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(null=False, blank=False, default=0, validators=[MinValueValidator(5), MaxValueValidator(20)])

    def add_robot_name(self, robots_runs):
        for robot_run in robots_runs:
            try:
                robot = Robot.objects.get(id=robot_run.get("id"))
                robot_run["name"] = robot.name

            except ObjectDoesNotExist:
                robot_run["name"] = ""

        return robots_runs

    class Meta:
        ordering = ["-distance"]

    def get_filtered_robot_runs(self, status):
        if status == "all":
            robots_runs = RobotRun.objects.filter().values()
        else:
            robots_runs = RobotRun.objects.filter(status=status).values()

        return robots_runs

    def get_robots_runs_statuses(self):
        statuses = RobotRun.objects.filter().values('status')

        all_robots_runs_statuses = []

        for item in statuses:
            all_robots_runs_statuses.append(item.get("status"))

        distinct_robots_runs_statuses = list(set(all_robots_runs_statuses))

        postprocessed_robots_runs_statuses = []

        for item in distinct_robots_runs_statuses:
            postprocessed_robots_runs_statuses.append({"status": item})

        postprocessed_robots_runs_statuses.append({"status": "all"})

        return postprocessed_robots_runs_statuses
