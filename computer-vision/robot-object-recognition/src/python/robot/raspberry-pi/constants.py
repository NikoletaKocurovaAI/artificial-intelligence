class RpiPinsConstants:
    """
    This class explains how to connect two DC motors to L293D motor controller.

    Motor 1 connects to L293D's pins Enable, Input 1 and Input 2.
    Motor 2 connects to L293D's pins Enable 2, Input 3 and Input 4.
    """

    motor1_enable = 25
    motor1_input1 = 24
    motor1_input2 = 23
    motor2_enable2 = 17
    motor2_input3 = 22
    motor2_input4 = 27


class RpiPwm:
    """
    This class set-ups the Pulse With Modulation (PWM) for a motor control.
    """

    # TODO: the lower the frequency, the faster motor 1 runs. This is unexpected behavior.
    pwm_frequency_motor1 = 40
    duty_cycle_motor1 = 40
    pwm_frequency_motor2 = 40
    duty_cycle_motor2 = 40
