from django.db.models import Model, DateTimeField, TextField, IntegerField, CharField


class Robot(Model):
    name = CharField(max_length=128)
    motor_type = CharField(max_length=128)


class RobotRun(Model):
    robot_id = IntegerField(null=False, blank=False, default=0) # ForeignKey(Genre, on_delete=DO_NOTHING); min_value=1, max_value=10
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(null=False, blank=False, default=0) # min_value=1, max_value=1

    class Meta:
        ordering = ["distance"] # TODO asc or desc ?
