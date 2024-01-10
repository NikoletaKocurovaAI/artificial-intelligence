from django.db.models import Model, DateTimeField, TextField, IntegerField


class Robot(Model):
    name = TextField(null=False, blank=False)
    motor_type = TextField(null=False, blank=False)


class RobotRun(Model):
    robot_id = TextField(null=False, blank=False, default=0)
    started = DateTimeField(auto_now_add=False, default="")
    finished = DateTimeField(auto_now_add=False, default="")
    status = TextField(null=False, blank=False, default="")
    distance = IntegerField(null=False, blank=False, default=0)
