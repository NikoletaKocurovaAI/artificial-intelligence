class RpiPinsConstants:
    """
    This class explains how to connect two DC motors to L293D motor controller.

    Motor 1 connects to L293D's pins Enable, Input 1 and Input 2.
    Motor 2 connects to L293D's pins Enable 2, Input 3 and Input 4.
    """

    MOTOR1_ENABLE: int = 25
    MOTOR1_INPUT1: int = 24
    MOTOR1_INPUT2: int = 23
    MOTOR2_ENABLE2: int = 17
    MOTOR2_INPUT3: int = 22
    MOTOR2_INPUT4: int = 27

    MOTOR1_IR_SPEED_SENSOR_PIN: int = 14
    MOTOR1_ENCODER_CHANNEL_B_PIN: int = 6  # todo remove/replace
    NO_PULSES_PER_MOTOR_REVOLUTION: int = 2
    IR_SPEED_SENSOR_TIMEOUT: int = 1  # 1 second timeout for zero RPM (Revolutions per minute)


class RpiPwmConstants:
    """
    This class set-ups the Pulse With Modulation (PWM) for a motor control.
    """

    PWM_FREQUENCY_MOTOR1: int = 5
    DUTY_CYCLE_MOTOR1: int = 5

    PWM_FREQUENCY_MOTOR2: int = 40
    DUTY_CYCLE_MOTOR2: int = 40


class DistanceTrackerConstants:
    ALLOWED_DISTANCE_TOTAL_ROTATIONS: int = 20
    ALLOWED_DISTANCE_FROM_OBJECT_PX: int = 5

    # Set the real size of the object (in millimeters) and the focal length of the camera (in millimeters)
    REAL_OBJECT_SIZE_MM: int = 100  # Example: Size of an object in millimeters
    FOCAL_LENGTH_MM: int = 1000  # Example: Focal length of the camera in millimeters


class ObjectDetectorConstants:
    CONFIDENCE: float = 0.5
