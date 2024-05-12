import cv2
import numpy as np
from cv2 import dnn_Net
from typing import Sequence

from constants import ObjectDetectorConstants as detector_cons
from position_estimator import position_estimator


class ObjectDetector:
    @staticmethod
    def load_yolov3() -> (dnn_Net, list):
        print("loading yolo weights")

        net: dnn_Net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")

        layer_names: Sequence[str] = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        print(f"net {net}")
        print(f"output_layers {output_layers}")

        return net, output_layers

    @staticmethod
    def detect_objects(net, output_layers, frame) -> None:
        print(f"detecting objects")

        # Perform object detection
        blob = cv2.dnn.blobFromImage(
            frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
        )
        net.setInput(blob)
        outs = net.forward(output_layers)

        is_detecting_objects_enabled: bool = True

        print(f"outs {outs}")

        # Process each detected object
        for out in outs:
            for detection in out:
                print(f"detection in out {detection}")

                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > detector_cons.CONFIDENCE:
                    print("confidence higher than 0.5")

                    # Get object coordinates
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])

                    # Draw bounding box
                    cv2.rectangle(
                        frame,
                        (center_x - w // 2, center_y - h // 2),
                        (center_x + w // 2, center_y + h // 2),
                        (255, 0, 0),
                        2,
                    )

                    if position_estimator.should_robot_avoid_object(
                        frame, center_x, center_y
                    ):
                        is_detecting_objects_enabled = False

                        break

            if not is_detecting_objects_enabled:
                position_estimator.avoid_object()

                break

        cv2.imshow("Frame", frame)


object_detector = ObjectDetector()
