import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwm as pwm


class MotorController:
    """
    This class sets control pins.
    """
    def __init__(self):
        # Set the pin numbering mode to BCM
        self.pin_numbering_mode = GPIO.BCM

        # Set up motor 1 & 2 enable control pins
        GPIO.setup(pins.motor1_enable, GPIO.OUT)
        GPIO.setup(pins.motor2_enable2, GPIO.OUT)

        # Set up motor 1 & 2 PWM and duty cycle
        pwm_motor1 = GPIO.PWM(pins.motor1_enable, pwm.pwm_frequency)
        pwm_motor1.start(pwm.duty_cycle)
        pwm_motor2 = GPIO.PWM(pins.motor2_enable2, pwm.pwm_frequency)
        pwm_motor2.start(pwm.duty_cycle)

        # Set up motor 1 IO control pins
        GPIO.setup(pins.motor1_input1, GPIO.OUT)
        GPIO.setup(pins.motor1_input2, GPIO.OUT)

        # Set up motor 2 IO control pins
        GPIO.setup(pins.motor2_input3, GPIO.OUT)
        GPIO.setup(pins.motor2_input4, GPIO.OUT)

    def run(self) -> None:
        print("Moving forwards")

        GPIO.setmode(self.pin_numbering_mode)

        GPIO.output(pins.motor1_input1, GPIO.HIGH)
        GPIO.output(pins.motor1_input2, GPIO.LOW)
        GPIO.output(pins.motor1_enable, GPIO.HIGH)

        GPIO.output(pins.motor2_input3, GPIO.HIGH)
        GPIO.output(pins.motor2_input4, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.HIGH)

    def stop(self) -> None:
        print("Stopping")

        GPIO.setmode(self.pin_numbering_mode)

        GPIO.output(pins.motor1_enable, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.LOW)

        GPIO.cleanup()

    def turn(self, direction: str) -> None:
        GPIO.setmode(self.pin_numbering_mode)

        if direction == "right":
            print("Rotating right")

            GPIO.output(pins.motor1_input1, GPIO.HIGH)
            GPIO.output(pins.motor1_input2, GPIO.LOW)
            GPIO.output(pins.motor1_enable, GPIO.HIGH)


motor_controller = MotorController()
