import time

from motor_controller import motor_controller
from object_detector import object_detector


def main():
    object_detector.take_picture()

    # motor_controller.run("forwards")
    # time.sleep(3)

    # motor_controller.stop()


if __name__ == "__main__":
    main()
