import cv2
import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, DistanceTrackerConstants as tracker


class PositionEstimator:
    """
    Counting wheels rotations, recognize how far the robot went.
    """

    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # GPIO.IN This constant is used to configure a GPIO pin as an input pin. It indicates that the GPIO pin will be
    # used to read external signals or data from sensors.
    # GPIO.PUD_UP enables the internal pull-up resistor on the GPIO pin, ensuring a defined logic level
    GPIO.setup(pins.MOTOR1_ENCODER_CHANNEL_A_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pins.MOTOR1_ENCODER_CHANNEL_B_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # rotations_counter: int = 0

    # @staticmethod
    # def _handle_rotation_event() -> int:
    #     global rotations_counter
    #     if GPIO.input(pins.MOTOR1_ENCODER_CHANNEL_B_PIN):
    #         rotations_counter += 1
    #     else:
    #         rotations_counter -= 1
    #
    #     return rotations_counter

    @staticmethod
    def _calculate_distance_rotations_total() -> int:
        # _handle_rotation_event()
        return 20

    def should_robot_continue(self) -> bool:
        no_rotations: int = self._calculate_distance_rotations_total()

        return no_rotations == tracker.ALLOWED_DISTANCE_TOTAL_ROTATIONS

    @staticmethod
    def _calculate_distance_from_object(frame) -> int:
        # return (REAL_OBJECT_SIZE_MM * FOCAL_LENGTH_MM) / object_size_pixels
        return 5

    def should_robot_avoid_object(self, frame, center_x: int, center_y: int) -> bool:
        distance_from_object: int = self._calculate_distance_from_object(frame)

        # Display distance on frame
        cv2.putText(
            frame,
            f"Distance: {distance_from_object:.2f} mm",
            (center_x, center_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

        return distance_from_object <= tracker.ALLOWED_DISTANCE_FROM_OBJECT_PX

    @staticmethod
    def avoid_object() -> None:
        pass


position_estimator = PositionEstimator()
