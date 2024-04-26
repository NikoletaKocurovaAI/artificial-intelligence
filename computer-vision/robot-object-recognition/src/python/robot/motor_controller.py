import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwm as pwm


class MotorController:
    """
    This class sets control pins, runs the robot and turns it left or right.
    """
    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up motor 1 & 2 enable control pins
    GPIO.setup(pins.motor1_enable, GPIO.OUT)
    GPIO.setup(pins.motor2_enable2, GPIO.OUT)

    # Set up motor 1 & 2 PWM and duty cycle
    pwm_motor1 = GPIO.PWM(pins.motor1_enable, pwm.pwm_frequency_motor1)
    pwm_motor1.start(pwm.duty_cycle_motor1)
    pwm_motor2 = GPIO.PWM(pins.motor2_enable2, pwm.pwm_frequency_motor2)
    pwm_motor2.start(pwm.duty_cycle_motor2)

    # Set up motor 1 IO control pins
    GPIO.setup(pins.motor1_input1, GPIO.OUT)
    GPIO.setup(pins.motor1_input2, GPIO.OUT)

    # Set up motor 2 IO control pins
    GPIO.setup(pins.motor2_input3, GPIO.OUT)
    GPIO.setup(pins.motor2_input4, GPIO.OUT)

    @staticmethod
    def run(direction: str) -> None:
        if direction == "forwards":
            GPIO.output(pins.motor1_input1, GPIO.HIGH)
            GPIO.output(pins.motor1_input2, GPIO.LOW)
            GPIO.output(pins.motor1_enable, GPIO.HIGH)

            GPIO.output(pins.motor2_input3, GPIO.HIGH)
            GPIO.output(pins.motor2_input4, GPIO.LOW)
            GPIO.output(pins.motor2_enable2, GPIO.HIGH)

        elif direction == "backwards":
            GPIO.output(pins.motor1_input1, GPIO.LOW)
            GPIO.output(pins.motor1_input2, GPIO.HIGH)
            GPIO.output(pins.motor1_enable, GPIO.HIGH)

            GPIO.output(pins.motor2_input3, GPIO.LOW)
            GPIO.output(pins.motor2_input4, GPIO.HIGH)
            GPIO.output(pins.motor2_enable2, GPIO.HIGH)

    @staticmethod
    def stop() -> None:
        GPIO.output(pins.motor1_enable, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.LOW)

        GPIO.cleanup()

    @staticmethod
    def turn(direction: str) -> None:
        if direction == "right":
            GPIO.output(pins.motor1_input1, GPIO.HIGH)
            GPIO.output(pins.motor1_input2, GPIO.LOW)
            GPIO.output(pins.motor1_enable, GPIO.HIGH)

            GPIO.output(pins.motor2_input3, GPIO.LOW)
            GPIO.output(pins.motor2_input4, GPIO.LOW)
            GPIO.output(pins.motor2_enable2, GPIO.LOW)

        elif direction == "left":
            GPIO.output(pins.motor1_input1, GPIO.LOW)
            GPIO.output(pins.motor1_input2, GPIO.LOW)
            GPIO.output(pins.motor1_enable, GPIO.LOW)

            GPIO.output(pins.motor2_input3, GPIO.HIGH)
            GPIO.output(pins.motor2_input4, GPIO.LOW)
            GPIO.output(pins.motor2_enable2, GPIO.HIGH)


motor_controller = MotorController()
