from typing import Optional

from .tests.testing_data import ROBOT, ROBOT_RUN


class Crud:
    @staticmethod
    def get_list(status: Optional[str] = None):
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # robot_run = RobotRun.objects.get(status="") # all, by status
        # fk in robot run is robot.id
        # robot = Robot.objects.get(id="
        # robot.robotRun

        return ROBOT_RUN

    @staticmethod
    def get_one(id: str):
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # robot = Robot.objects.get(id=)

        return ROBOT[1]

    @staticmethod
    def create_one():
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # register new robot
        # robot = Robot.objects.create(name="", ...)
        # if not.user.is_authenticated
        # return robot detail with newly created one

        pass

    @staticmethod
    def update_one():
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # schedule robot's next run
        # robot =
        # robot.set()
        # if not.user.is_authenticated

        pass

    @staticmethod
    def delete_one():
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # Robot.objects.get(id="").delete()
        # Delete also robot run records
        # if not.user.is_authenticated
        # return redirect robot run

        pass
