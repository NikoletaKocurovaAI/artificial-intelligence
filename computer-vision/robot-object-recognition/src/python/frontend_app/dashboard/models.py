from django.db.models import Model, DateTimeField, TextField, IntegerField, CharField


class Robot(Model):
    name = CharField(max_length=128, null=False, blank=False, default="")
    motor_type = CharField(max_length=128, null=False, blank=False, default="")

    def validate_name(self):
        # TODO validate method or CharField unique=True
        pass


class RobotRun(Model):
    robot_id = IntegerField(null=False, blank=False, default=0) # ForeignKey(Genre, on_delete=DO_NOTHING); min_value=1, max_value=10
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(null=False, blank=False, default=0) # TODO validators=[MinValueValidator(limit_value=5), max_value=20

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
