import RPi.GPIO as GPIO
import time
import threading
# import cv2

from constants import RpiPinsConstants as pins
from motor_controller import motor_controller
#from object_detector import object_detector
#from position_estimator import position_estimator


# Set the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor 1 IR speed sensor
GPIO.setup(pins.MOTOR1_IR_SPEED_SENSOR_PIN, GPIO.IN)

motor1_rotations_counter = 0
motor1_running = False


def read_ir_sensor_pulses() -> None:
    global motor1_rotations_counter, motor1_running

    while motor1_running:
        if GPIO.input(14):
            motor1_rotations_counter += 1
            print(f"IR sensor input {GPIO.input(14)}")


def main():
    global motor1_running
    # net, output_layers = object_detector.load_yolov3()
    # camera = cv2.VideoCapture(0)

    # running_robot_enabled: bool = True
    start_time: float = time.time()

    ir_sensor = threading.Thread(target=read_ir_sensor_pulses)
    ir_sensor.start()

    motor1_running = True
    motor_controller.run("forwards")

    # while running_robot_enabled:
    while time.time() - start_time < 8:
        continue

        # print("reading frame")
        #
        # ret, frame = camera.read()
        #
        # if not ret:
        #     break

        # object_detector.detect_objects(net, output_layers, frame)

        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    motor1_running = False
    ir_sensor.join()

    print(f"No of rotations {motor1_rotations_counter}")

    motor_controller.stop()

    # Release camera and close windows
    # camera.release()
    # cv2.destroyAllWindows()

    # position_estimator.control_led("off")


if __name__ == "__main__":
    main()
