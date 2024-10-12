import time
import cv2

from exceptions import CameraNotOpenedException, CameraFrameNotCapturedException
from motor_controller import motor_controller
# from object_detector import object_detector
# from position_estimator import position_estimator


def main():
    # running_robot_enabled: bool = True
    # position_estimator.start()

    # net, output_layers = object_detector.load_yolov3()

    # print("Initializing camera")

    # camera = cv2.VideoCapture(0)
    # fourcc: int = cv2.VideoWriter_fourcc(*'XVID')
    # camera_file_output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    #
    # if not camera.isOpened():
    #     raise CameraNotOpenedException

    # start_time: float = time.time()

    motor_controller.run("forwards")
    time.sleep(2)

    motor_controller.turn("right")
    time.sleep(4)

    motor_controller.turn("left")
    time.sleep(4)

    # print("Capturing camera frame")

    # while time.time() - start_time < 5:
    #     ret, frame = camera.read()
    #
    #     if not ret:
    #         raise CameraFrameNotCapturedException
    #
    #     camera_file_output.write(frame)

        # object_detector.detect_objects(net, output_layers, frame)
        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    motor_controller.stop()

    # position_estimator.stop()
    # print(f"No of rotations {position_estimator.get_rotations_count()}")

    # camera.release()
    # camera_file_output.release()


if __name__ == "__main__":
    main()
