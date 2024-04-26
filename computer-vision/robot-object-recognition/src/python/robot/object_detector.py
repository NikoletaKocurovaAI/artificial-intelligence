import cv2
import numpy as np
from cv2 import dnn_Net
from typing import Sequence


class ObjectDetector:
    @staticmethod
    def load_yolov3() -> (dnn_Net, list):
        net: dnn_Net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

        layer_names: Sequence[str] = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        return net, output_layers

    @staticmethod
    def _calculate_distance(frame) -> int:
        # return (real_object_size_mm * focal_length_mm) / object_size_pixels
        return 5

    def detect_objects(self, net, output_layers, frame):
        # Perform object detection
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Process each detected object
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
                    # Get object coordinates
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])

                    # Draw bounding box
                    cv2.rectangle(frame, (center_x - w // 2, center_y - h // 2), (center_x + w // 2, center_y + h // 2),
                                  (255, 0, 0), 2)

                    # Calculate distance from object size
                    distance = self._calculate_distance(frame)

                    # Display distance on frame
                    cv2.putText(frame, f"Distance: {distance:.2f} mm", (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 255, 0), 2)

        cv2.imshow("Frame", frame)


object_detector = ObjectDetector()
