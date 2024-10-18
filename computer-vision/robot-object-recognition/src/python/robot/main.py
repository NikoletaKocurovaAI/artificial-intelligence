import threading
import time

from motor_controller import MotorController
from object_detector import object_detector
# from position_estimator import position_estimator


def main():
    # TODO
    # running_robot_enabled: bool = True
    # position_estimator.start()

    net, output_layers = object_detector.load_yolov3()

    camera_thread = threading.Thread(target=object_detector.start_video_capture)
    camera_thread.start()

    print("Robot is waiting to start")
    time.sleep(4)

    motor_controller = MotorController()

    motor_controller.run("forwards")
    time.sleep(2)

    motor_controller.turn("right")
    time.sleep(4)

    motor_controller.turn("left")
    time.sleep(4)

    # TODO
    # while time.time() - start_time < 5:
        # camera running / start_video_capture()

        # object_detector.detect_objects(net, output_layers, frame)
        # running_robot_enabled: bool = position_estimator.should_robot_continue()

    motor_controller.stop()

    object_detector.stop_video_capture()
    camera_thread.join()

    # TODO
    # position_estimator.stop()
    # print(f"No of rotations {position_estimator.get_rotations_count()}")

    object_detector.detect_objects(net, output_layers)


if __name__ == "__main__":
    main()
