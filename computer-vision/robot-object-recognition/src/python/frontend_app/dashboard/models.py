from django.db.models import Model, DateTimeField, TextField


class Robot(Model):
    name = TextField(null=False, blank=False)
    motor_type = TextField(null=False, blank=False)


class RobotRun(Model):
    robot_id = TextField(null=True, blank=True)
    started = DateTimeField(auto_now_add=True)
    finished = DateTimeField(auto_now_add=True)
    status = TextField(null=True, blank=True)


class RobotStatus(Model):
    RUNNING = ""
    STOPPED = ""
    ERROR = ""
