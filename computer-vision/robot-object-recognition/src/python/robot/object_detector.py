import cv2


class ObjectDetector:
    def take_picture(self):
        # Initialize the camera
        cap = cv2.VideoCapture(0)

        try:
            # Check if the camera is opened successfully
            if not cap.isOpened():
                raise Exception("Could not open camera")

            # Capture a frame from the camera
            ret, frame = cap.read()

            # Check if the frame was captured successfully
            if not ret:
                raise Exception("Failed to capture image")

            # Save the captured frame to a file
            cv2.imwrite('image.jpg', frame)

            # Print a success message
            print("Image captured successfully")

        finally:
            # Release the camera resources
            cap.release()

object_detector = ObjectDetector()
