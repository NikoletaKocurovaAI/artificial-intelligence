import time
import RPi.GPIO as GPIO

from motor_controller import MotorController


def main():
    # start the run
    MotorController.run(GPIO.HIGH, GPIO.LOW, "Moving forwards")
    time.sleep(3)

    MotorController.run(GPIO.LOW, GPIO.HIGH, "Moving backwards")
    time.sleep(3)

    MotorController.stop()


if __name__ == "__main__":
    main()