from django.db.models import Model, DateTimeField, TextField, IntegerField, CharField


class Robot(Model):
    name = CharField(max_length=128, null=False, blank=False, default="")
    motor_type = CharField(max_length=128, null=False, blank=False, default="")


class RobotRun(Model):
    robot_id = IntegerField(null=False, blank=False, default=0) # ForeignKey(Genre, on_delete=DO_NOTHING); min_value=1, max_value=10
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(null=False, blank=False, default=0) # TODO validators=[MinValueValidator(limit_value=5), max_value=20

    class Meta:
        ordering = ["-distance"]
