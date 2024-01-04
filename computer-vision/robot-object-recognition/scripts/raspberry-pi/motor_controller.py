import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwm as pwm


class MotorController:
    """
    This class sets control pins, runs the robot and turns it left or right.
    """
    @staticmethod
    def run() -> None:
        print("Moving forwards")

        # Set the pin numbering mode
        GPIO.setmode(GPIO.BCM)

        # Set up control pins
        GPIO.setup(pins.motor1_enable, GPIO.OUT)
        GPIO.setup(pins.motor2_enable2, GPIO.OUT)
        GPIO.setup(pins.motor1_input1, GPIO.OUT)
        GPIO.setup(pins.motor1_input2, GPIO.OUT)
        GPIO.setup(pins.motor2_input3, GPIO.OUT)
        GPIO.setup(pins.motor2_input4, GPIO.OUT)

        # Set up motor PWM and duty cycle
        pwm_motor1 = GPIO.PWM(pins.motor1_enable, pwm.pwm_frequency_motor1)
        pwm_motor1.start(pwm.duty_cycle_motor1)
        pwm_motor2 = GPIO.PWM(pins.motor2_enable2, pwm.pwm_frequency_motor2)
        pwm_motor2.start(pwm.duty_cycle_motor2)

        # Run motor 1
        GPIO.output(pins.motor1_input1, GPIO.HIGH)
        GPIO.output(pins.motor1_input2, GPIO.LOW)
        GPIO.output(pins.motor1_enable, GPIO.HIGH)

        # Run motor 2
        GPIO.output(pins.motor2_input3, GPIO.HIGH)
        GPIO.output(pins.motor2_input4, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.HIGH)

    @staticmethod
    def stop() -> None:
        print("Stopping")

        # Set the pin numbering mode
        GPIO.setmode(GPIO.BCM)

        # Set up control pins
        GPIO.setup(pins.motor1_enable, GPIO.OUT)
        GPIO.setup(pins.motor2_enable2, GPIO.OUT)

        GPIO.output(pins.motor1_enable, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.LOW)

        GPIO.cleanup()

    @staticmethod
    def turn(direction: str) -> None:
        # Set the pin numbering mode
        GPIO.setmode(GPIO.BCM)

        # Set up control pins
        GPIO.setup(pins.motor1_enable, GPIO.OUT)
        GPIO.setup(pins.motor2_enable2, GPIO.OUT)
        GPIO.setup(pins.motor1_input1, GPIO.OUT)
        GPIO.setup(pins.motor1_input2, GPIO.OUT)
        GPIO.setup(pins.motor2_input3, GPIO.OUT)
        GPIO.setup(pins.motor2_input4, GPIO.OUT)

        # Set up motor PWM and duty cycle
        pwm_motor1 = GPIO.PWM(pins.motor1_enable, pwm.pwm_frequency_motor1)
        pwm_motor1.start(pwm.duty_cycle_motor1)
        pwm_motor2 = GPIO.PWM(pins.motor2_enable2, pwm.pwm_frequency_motor2)
        pwm_motor2.start(pwm.duty_cycle_motor2)

        # turning is achieved by driving one wheel forward while reversing the other.
        if direction == "right":
            print("Rotating right")

            # Run motor 1
            GPIO.output(pins.motor1_input1, GPIO.HIGH)
            GPIO.output(pins.motor1_input2, GPIO.LOW)

            # Stop motor 2
            GPIO.output(pins.motor2_input3, GPIO.LOW)
            GPIO.output(pins.motor2_input4, GPIO.HIGH)

        # enable the left motor to move backward while the right motor moves forward
        elif direction == "left":
            print("Rotating left")

            # Run motor 1
            GPIO.output(pins.motor1_input1, GPIO.LOW)
            GPIO.output(pins.motor1_input2, GPIO.HIGH)

            # Stop motor 2
            GPIO.output(pins.motor2_input3, GPIO.HIGH)
            GPIO.output(pins.motor2_input4, GPIO.LOW)

motor_controller = MotorController()
