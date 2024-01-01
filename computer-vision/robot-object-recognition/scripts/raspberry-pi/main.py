import time

from motor_controller import motor_controller


def main():
    motor_controller.run()

    time.sleep(3)

    motor_controller.stop()

    time.sleep(3)

    motor_controller.turn("right")


if __name__ == "__main__":
    main()