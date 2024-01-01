import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwm as pwm


class MotorController:
    """
    This class sets control pins.
    """
    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

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

    @staticmethod
    def run(signal1: int, signal2: int, message: str) -> None:
        print(message)
            # motor 1
        GPIO.output(pins.motor1_input1, signal1)
        GPIO.output(pins.motor1_input2, signal2)
        GPIO.output(pins.motor1_enable, GPIO.HIGH)

            # motor 2
        GPIO.output(pins.motor2_input3, signal1)
        GPIO.output(pins.motor2_input4, signal2)
        GPIO.output(pins.motor2_enable2, GPIO.HIGH)

    @staticmethod
    def stop() -> None:
        print("Stopping")
        GPIO.output(pins.motor1_enable, GPIO.LOW)
        GPIO.output(pins.motor2_enable2, GPIO.LOW)

        print("Cleaning up")
        GPIO.cleanup()
