import time
import RPi.GPIO as GPIO

from motor_controller import MotorController


def main():
    MotorController.run()

    time.sleep(3)

    MotorController.stop()

    MotorController.turn("right")

    time.sleep(3)

    MotorController.stop()


if __name__ == "__main__":
    main()