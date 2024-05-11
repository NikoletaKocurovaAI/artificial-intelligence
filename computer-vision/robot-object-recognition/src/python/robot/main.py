import cv2

# from motor_controller import motor_controller
from object_detector import object_detector
from position_estimator import position_estimator


def main():
    net, output_layers = object_detector.load_yolov3()
    camera = cv2.VideoCapture(0)

    # motor_controller.run("forwards")

    while position_estimator.should_robot_continue():
        print("reading frame")

        ret, frame = camera.read()
        if not ret:
            break

        object_detector.detect_objects(net, output_layers, frame)

    # motor_controller.stop()

    # Release camera and close windows
    camera.release()
    cv2.destroyAllWindows()

    # position_estimator.control_led("off")


if __name__ == "__main__":
    main()
