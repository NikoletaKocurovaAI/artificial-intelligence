import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins


class PositionEstimator:
    """
    Counting wheels rotations, recognize how far the robot went.
    """
    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # GPIO.IN This constant is used to configure a GPIO pin as an input pin. It indicates that the GPIO pin will be
    # used to read external signals or data from sensors.
    # GPIO.PUD_UP enables the internal pull-up resistor on the GPIO pin, ensuring a defined logic level
    GPIO.setup(pins.motor1_encoder_channelA_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pins.motor1_encoder_channelB_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    rotations_counter: int = 0

    @staticmethod
    def _handle_rotation_event() -> int:
        global rotations_counter
        if GPIO.input(pins.motor1_encoder_channelB_pin):
            rotations_counter += 1
        else:
            rotations_counter -= 1

        return rotations_counter

    @staticmethod
    def should_robot_continue() -> bool:
        return True


position_estimator = PositionEstimator()
