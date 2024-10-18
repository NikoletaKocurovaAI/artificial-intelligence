import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwmConstants as pwm


class MotorController:
    """
    This class sets control pins, runs the robot and turns it left or right.
    """
    def __init__(self) -> None:
        print("Initializing motor controller")

        # Set the pin numbering mode to BCM
        GPIO.setmode(GPIO.BCM)

        # Set up motor 1 & 2 enable control pins
        GPIO.setup(pins.MOTOR1_ENABLE, GPIO.OUT)
        GPIO.setup(pins.MOTOR2_ENABLE2, GPIO.OUT)

        # Set up motor 1 & 2 PWM and duty cycle
        self.pwm_motor1 = GPIO.PWM(pins.MOTOR1_ENABLE, pwm.PWM_FREQUENCY_MOTOR1)
        self.pwm_motor1.start(0)
        self.pwm_motor2 = GPIO.PWM(pins.MOTOR2_ENABLE2, pwm.PWM_FREQUENCY_MOTOR2)
        self.pwm_motor2.start(0)

        # Set up motor 1 IO control pins
        GPIO.setup(pins.MOTOR1_INPUT1, GPIO.OUT)
        GPIO.setup(pins.MOTOR1_INPUT2, GPIO.OUT)

        # Set up motor 2 IO control pins
        GPIO.setup(pins.MOTOR2_INPUT3, GPIO.OUT)
        GPIO.setup(pins.MOTOR2_INPUT4, GPIO.OUT)

    def run(self, direction: str) -> None:
        if direction == "forwards":
            print("Running robot forwards")

            GPIO.output(pins.MOTOR1_INPUT1, GPIO.LOW)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.LOW)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.HIGH)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)

            self.pwm_motor1.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR1)
            self.pwm_motor2.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR2)

        elif direction == "backwards":
            print("Running robot backwards")

            GPIO.output(pins.MOTOR1_INPUT1, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.HIGH)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)

            self.pwm_motor1.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR1)
            self.pwm_motor2.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR2)

    @staticmethod
    def stop() -> None:
        print("Stopped robot")

        GPIO.output(pins.MOTOR1_ENABLE, GPIO.LOW)
        GPIO.output(pins.MOTOR2_ENABLE2, GPIO.LOW)

        GPIO.cleanup()

    def turn(self, direction: str) -> None:
        if direction == "right":
            print("Turning right")
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.LOW)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.LOW)

            self.pwm_motor1.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR1)

        elif direction == "left":
            print("Turning left")
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.LOW)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.LOW)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.HIGH)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)

            self.pwm_motor2.ChangeDutyCycle(pwm.DUTY_CYCLE_MOTOR2)
