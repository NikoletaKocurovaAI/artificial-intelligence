from typing import Optional

import RPi.GPIO as GPIO
import time
# import cv2

from constants import RpiPinsConstants as pins
from motor_controller import motor_controller
#from object_detector import object_detector
#from position_estimator import position_estimator


# Set the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor 1 IR speed sensor
# use the GPIO.IN to read signals from the sensor
# pull_up_down sets the internal pull-up resistor for the pin (handles RPI's voltage logic)
GPIO.setup(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

last_time_pulse_measured: Optional[float] = None


def on_pulse_event(channel: int) -> None:
    """
    :param channel: In the RPi.GPIO lib, an event detection callback function of is called with the channel arg,
    which is the pin number, where the event was detected.
    """
    global last_time_pulse_measured

    if last_time_pulse_measured:
        print(f"The event detected on the RPi pin {channel}")

        period_between_pulses: float = time.time() - last_time_pulse_measured
        print(f"Detected the period between pulses {period_between_pulses}")

        last_time_pulse_measured: float = time.time()


def main():
    # net, output_layers = object_detector.load_yolov3()
    # camera = cv2.VideoCapture(0)

    GPIO.add_event_detect(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.RISING, callback=on_pulse_event)

    # running_robot_enabled: bool = True
    start_time: float = time.time()

    # while running_robot_enabled:
    while time.time() - start_time < 30:
        motor_controller.run("forwards")

        print(f"Last time the IR sensor pulse measured: {last_time_pulse_measured}")

        # print("reading frame")
        #
        # ret, frame = camera.read()
        #
        # if not ret:
        #     break

        # object_detector.detect_objects(net, output_layers, frame)

        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    motor_controller.stop()

    # Release camera and close windows
    # camera.release()
    # cv2.destroyAllWindows()

    # position_estimator.control_led("off")


if __name__ == "__main__":
    main()
