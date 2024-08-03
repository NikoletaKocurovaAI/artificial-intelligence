from typing import Optional
import time

import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, RpiPwmConstants as pwm


class MotorController:
    """
    This class sets control pins, runs the robot and turns it left or right.
    """
    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up motor 1 & 2 enable control pins
    GPIO.setup(pins.MOTOR1_ENABLE, GPIO.OUT)
    # GPIO.setup(pins.MOTOR2_ENABLE2, GPIO.OUT)

    # Set up motor 1 & 2 PWM and duty cycle
    pwm_motor1 = GPIO.PWM(pins.MOTOR1_ENABLE, pwm.PWM_FREQUENCY_MOTOR1)
    pwm_motor1.start(pwm.DUTY_CYCLE_MOTOR1)
    # pwm_motor2 = GPIO.PWM(pins.MOTOR2_ENABLE2, pwm.PWM_FREQUENCY_MOTOR2)
    # pwm_motor2.start(pwm.DUTY_CYCLE_MOTOR2)

    # Set up motor 1 IO control pins
    GPIO.setup(pins.MOTOR1_INPUT1, GPIO.OUT)
    GPIO.setup(pins.MOTOR1_INPUT2, GPIO.OUT)

    # Set up motor 2 IO control pins
    # GPIO.setup(pins.MOTOR2_INPUT3, GPIO.OUT)
    # GPIO.setup(pins.MOTOR2_INPUT4, GPIO.OUT)

    # Set up motor 1 IR speed sensor
    # use the GPIO.IN to read signals from the sensor
    # pull_up_down sets the internal pull-up resistor for the pin (handles RPI's voltage logic)
    GPIO.setup(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __init__(self, last_time_pulse_measured: Optional[float]) -> None:
        self.last_time_pulse_measured: Optional[float] = last_time_pulse_measured

        GPIO.add_event_detect(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.RISING, callback=self.on_pulse_event)

    def on_pulse_event(self, channel: int) -> None:
        """
        :param channel: In the RPi.GPIO lib, an event detection callback function of is called with the channel arg,
        which is the pin number, where the event was detected.
        """
        if self.last_time_pulse_measured:
            print(f"The event detected on the RPi pin {channel}")

            period_between_pulses: float = time.time() - self.last_time_pulse_measured
            print(f"Detected the period between pulses {period_between_pulses}")

            self.last_time_pulse_measured: float = time.time()

    @staticmethod
    def run(direction: str) -> None:
        if direction == "forwards":
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            # GPIO.output(pins.MOTOR2_INPUT3, GPIO.HIGH)
            # GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            # GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)

        elif direction == "backwards":
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.LOW)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.LOW)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.HIGH)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)

    @staticmethod
    def stop() -> None:
        GPIO.output(pins.MOTOR1_ENABLE, GPIO.LOW)
        # GPIO.output(pins.MOTOR2_ENABLE2, GPIO.LOW)

        GPIO.cleanup()

    @staticmethod
    def turn(direction: str) -> None:
        if direction == "right":
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.HIGH)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.HIGH)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.LOW)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.LOW)

        elif direction == "left":
            GPIO.output(pins.MOTOR1_INPUT1, GPIO.LOW)
            GPIO.output(pins.MOTOR1_INPUT2, GPIO.LOW)
            GPIO.output(pins.MOTOR1_ENABLE, GPIO.LOW)

            GPIO.output(pins.MOTOR2_INPUT3, GPIO.HIGH)
            GPIO.output(pins.MOTOR2_INPUT4, GPIO.LOW)
            GPIO.output(pins.MOTOR2_ENABLE2, GPIO.HIGH)
