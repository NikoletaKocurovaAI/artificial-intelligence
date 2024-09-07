import threading
from typing import Optional

import cv2
import RPi.GPIO as GPIO

from constants import RpiPinsConstants as pins, DistanceTrackerConstants as tracker


class PositionEstimator:
    """
    Counting wheels rotations, recognize how far the robot went.

    This class uses the Encapsulation design pattern, which is a fundamental principle of object-oriented
    programming. Encapsulation means combining the data (attributes) and methods (functions) into a single class, and
    restricting access to some of the object's components.
    """

    # Set the pin numbering mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set up motor 1 IR speed sensor
    GPIO.setup(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.IN)

    def __init__(self) -> None:
        self.motor1_rotations_counter: int = 0
        self.motor1_running: bool = False
        self.motor1_ir_sensor_run: Optional[threading.Thread] = None

    def _read_ir_sensor_pulses(self) -> None:
        while self.motor1_running:
            if GPIO.input(pins.MOTOR1_IR_SPEED_SENSOR_PIN):
                self.motor1_rotations_counter += 1

    def start(self) -> None:
        self.motor1_running: bool = True

        self.motor1_ir_sensor_run = threading.Thread(target=self._read_ir_sensor_pulses)
        self.motor1_ir_sensor_run.start()

    def stop(self):
        self.motor1_running: bool = False

        if self.motor1_ir_sensor_run is not None:
            self.motor1_ir_sensor_run.join()

    def get_rotations_count(self) -> int:
        return self.motor1_rotations_counter

    @staticmethod
    def _calculate_distance_rotations_total() -> int:
        """
        Calculate the total distance traveled by the differential wheeled robot based on the number of rotations.
        """
        # self.get_rotations_count()
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
