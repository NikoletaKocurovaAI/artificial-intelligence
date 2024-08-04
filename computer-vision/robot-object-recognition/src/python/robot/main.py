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
GPIO.setup(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.IN)


def main():
    # net, output_layers = object_detector.load_yolov3()
    # camera = cv2.VideoCapture(0)

    # running_robot_enabled: bool = True
    start_time: float = time.time()
    rotations_counter: int = 0

    motor_controller.run("forwards")

    # while running_robot_enabled:
    while time.time() - start_time < 8:
        if GPIO.input(14):
            rotations_counter += 1

        # print("reading frame")
        #
        # ret, frame = camera.read()
        #
        # if not ret:
        #     break

        # object_detector.detect_objects(net, output_layers, frame)

        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    print(f"No of rotations {rotations_counter}")
    motor_controller.stop()

    # Release camera and close windows
    # camera.release()
    # cv2.destroyAllWindows()

    # position_estimator.control_led("off")


if __name__ == "__main__":
    main()
