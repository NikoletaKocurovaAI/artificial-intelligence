import RPi.GPIO as GPIO
import time

Motor1E = 25 # Enable1
Motor1A = 24 #
Motor1B = 23 #
Motor2E = 17
Motor2A = 22
Motor2B = 27

# Set the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up motor control pins
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

pwm1 = GPIO.PWM(Motor1E, 100)
pwm1.start(50)

pwm2 = GPIO.PWM(Motor2E, 100)
pwm2.start(50)

for i in range(2):
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    print("moving forwards")

    time.sleep(3)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

    print("moving backwards")

    time.sleep(3)

print("stop")
GPIO.output(Motor1E, GPIO.LOW)
GPIO.output(Motor2E, GPIO.LOW)

print("clean up")
GPIO.cleanup()
