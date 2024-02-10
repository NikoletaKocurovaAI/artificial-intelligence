import time

from motor_controller import motor_controller


def main():
    motor_controller.turn("left")
    time.sleep(3)

    motor_controller.run("backwards")
    time.sleep(3)

    motor_controller.turn("right")
    time.sleep(3)

    motor_controller.run("forwards")
    time.sleep(3)

    motor_controller.stop()


if __name__ == "__main__":
    main()
