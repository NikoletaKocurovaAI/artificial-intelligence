import cv2
import numpy as np
from cv2 import dnn_Net
from datetime import datetime
from typing import Sequence

from constants import ObjectDetectorConstants as detector_cons
from exceptions import CameraNotOpenedException, CameraFrameNotCapturedException
# from position_estimator import position_estimator


class ObjectDetector:
    # A class variable to control the camera loop in start_video_capture()
    capturing = True

    @classmethod
    def start_video_capture(cls) -> None:
        # net, output_layers = object_detector.load_yolov3()

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

        while cls.capturing:
            ret, frame = camera.read()

            if not ret:
                print("Failed to capture frame.")
                raise CameraFrameNotCapturedException

            # cls.detect_objects(net, output_layers, frame)

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
    def detect_objects(net, output_layers) -> None:
        print(f"Detecting objects")

        start_time = datetime.now()
        print(f"Start Date and Time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        video_capture = cv2.VideoCapture("output.avi")

        if not video_capture.isOpened():
            print("Could not open the video")
            return

        # Get video properties
        frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video_capture.get(cv2.CAP_PROP_FPS))

        print(f"FPS {fps}")

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_writer = cv2.VideoWriter("output_detected.avi", fourcc, fps, (frame_width, frame_height))

        # Calculate the total number of frames to process for 5 seconds
        max_frames = 1 * fps

        print(f"Max frames set to {max_frames}")

        frame_count = 0  # Keep track of frames processed

        while frame_count < max_frames:
            print(f"Processing frame no {frame_count+1}")
            ret, frame = video_capture.read()
            if not ret:
                break  # Exit the loop if there are no more frames

            # Perform object detection
            blob = cv2.dnn.blobFromImage(
                frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
            )
            net.setInput(blob)
            outs = net.forward(output_layers)

            # print(f"Outs {outs}")

            # Process each detected object
            for out in outs:
                for detection in out:
                    # print(f"Detection in out {detection}")

                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]

                    # print(f"Confidence: {confidence}")

                    if confidence > detector_cons.CONFIDENCE:
                        print(f"Confidence higher than {detector_cons.CONFIDENCE}")

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

                        # Optionally, you can add labels here if you have class names

            # Write the processed frame to the output video
            video_writer.write(frame)
            frame_count += 1  # Increment the frame count

        # Release resources
        video_capture.release()
        video_writer.release()
        print("Object detection completed")

        end_time = datetime.now()
        print(f"End Date and Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        duration = end_time - start_time
        print(f"Duration: {duration}")

object_detector = ObjectDetector()
