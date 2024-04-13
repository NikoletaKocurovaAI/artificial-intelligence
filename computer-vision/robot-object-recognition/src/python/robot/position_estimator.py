import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins


class PositionEstimator:
    # TODO: Counting wheels rotations, recognize how far the robot went.
    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO pin as output
    GPIO.setup(pins.led_pin, GPIO.OUT)

    encoder_counter: int = 0

    @staticmethod
    def control_led(mode: str):
        if mode == "on":
            GPIO.output(pins.led_pin, GPIO.HIGH)
        else:
            GPIO.output(pins.led_pin, GPIO.LOW)

    @staticmethod
    def collect_encoder_data():
        state = GPIO.input(pins.encoder_pin)

