import RPi.GPIO as GPIO
import time

Motor1E = 25
Motor1A = 24
Motor1B = 23

GPIO.setmode(GPIO.BCM)

# Set up motor control pins
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

for i in range(2):
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("moving forwards")

    time.sleep(3)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    print("moving backwards")

    time.sleep(3)

print("stop")
GPIO.output(Motor1E, GPIO.LOW)

print("clean up")
GPIO.cleanup()