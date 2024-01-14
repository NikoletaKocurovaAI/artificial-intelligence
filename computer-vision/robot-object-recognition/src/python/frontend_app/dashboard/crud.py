from pydantic_settings import BaseSettings
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

from .tests.testing_data import ROBOT_RUN


class Crud:
    def __init__(self):
        load_dotenv()

        DB_NAME = os.getenv("DB_NAME")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_USER = os.getenv("DB_USER")
        DB_PORT = os.getenv("DB_PORT")

        DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

        self.engine = create_engine(
            DATABASE_URL, connect_args={}
        )

    def get_list(self, query: str):
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

        with self.engine.connect() as connection:
            result = connection.execute(text(query))

            return result

    def get_one_by_id(self, id: int):
        """
        This ..

        :param request:
        :return:
        :raises
        """
        # robot = Robot.objects.get(id=)

        with self.engine.connect() as connection:
            result = connection.execute(text('SELECT * FROM public."robot"'))

            for row in result:
                robot_id = row[0]

                if robot_id == id:
                    return [{"name": row[1], "motor_type": row[2]}]

        return None

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
