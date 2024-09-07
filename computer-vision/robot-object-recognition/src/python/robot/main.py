import RPi.GPIO as GPIO
import time
import threading
# import cv2

from motor_controller import motor_controller
#from object_detector import object_detector
from position_estimator import position_estimator


# Set the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)


def main():
    # running_robot_enabled: bool = True
    # position_estimator.start()

    # net, output_layers = object_detector.load_yolov3()
    # camera = cv2.VideoCapture(0)

    motor_controller.run("forwards")

    time.sleep(5)

    # while running_robot_enabled:

        # print("reading frame")
        #
        # ret, frame = camera.read()
        #
        # if not ret:
        #     break

        # object_detector.detect_objects(net, output_layers, frame)

        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    motor_controller.stop()

    # position_estimator.stop()
    # print(f"No of rotations {position_estimator.get_rotations_count()}")

    # Release camera and close windows
    # camera.release()
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
