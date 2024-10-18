import cv2
import numpy as np
from cv2 import dnn_Net
from typing import Sequence

from constants import ObjectDetectorConstants as detector_cons
from exceptions import CameraNotOpenedException, CameraFrameNotCapturedException
from position_estimator import position_estimator


class ObjectDetector:
    # A class variable to control the camera loop in start_video_capture()
    capturing = True

    @classmethod
    def start_video_capture(cls) -> None:
        net, output_layers = object_detector.load_yolov3()

        print("Initializing camera")

        camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        camera_file_output = cv2.VideoWriter(
            "output.avi",
            fourcc, 20.0, (640, 480)
        )

        if not camera.isOpened():
            print("Camera not opened.")
            raise CameraNotOpenedException

        print("Starting camera capture")

        # Capture frames for 10 seconds or as needed
        while cls.capturing:
            ret, frame = camera.read()

            if not ret:
                print("Failed to capture frame.")
                raise CameraFrameNotCapturedException

            cls.detect_objects(net, output_layers, frame)

            # Write the captured frame to the file
            camera_file_output.write(frame)

        # Release the camera and output file
        camera.release()
        camera_file_output.release()

        print("Camera capture ended")

    @classmethod
    def stop_video_capture(cls):
        cls.capturing = False

    @staticmethod
    def load_yolov3() -> (dnn_Net, list):
        print("Loading yolo weights")

        net: dnn_Net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")

        layer_names: Sequence[str] = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        # print(f"Net {net}")
        # print(f"Output_layers {output_layers}")

        return net, output_layers

    @staticmethod
    def detect_objects(net, output_layers, frame) -> None:
        print(f"Detecting objects")

        # Perform object detection
        blob = cv2.dnn.blobFromImage(
            frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
        )
        net.setInput(blob)
        outs = net.forward(output_layers)

        # is_detecting_objects_enabled: bool = True

        # print(f"Outs {outs}")

        # Process each detected object
        for out in outs:
            for detection in out:
                # print(f"Detection in out {detection}")

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                print(f"Confidence: {confidence}")

        #         if confidence > detector_cons.CONFIDENCE:
        #             print("confidence higher than 0.5")
        #
        #             # Get object coordinates
        #             center_x = int(detection[0] * frame.shape[1])
        #             center_y = int(detection[1] * frame.shape[0])
        #             w = int(detection[2] * frame.shape[1])
        #             h = int(detection[3] * frame.shape[0])
        #
        #             # Draw bounding box
        #             cv2.rectangle(
        #                 frame,
        #                 (center_x - w // 2, center_y - h // 2),
        #                 (center_x + w // 2, center_y + h // 2),
        #                 (255, 0, 0),
        #                 2,
        #             )

            #         if position_estimator.should_robot_avoid_object(
            #             frame, center_x, center_y
            #         ):
            #             is_detecting_objects_enabled = False
            #
            #             break
            #
            # if not is_detecting_objects_enabled:
            #     position_estimator.avoid_object()
            #
            #     break

        # cv2.imshow("Frame", frame)


object_detector = ObjectDetector()
