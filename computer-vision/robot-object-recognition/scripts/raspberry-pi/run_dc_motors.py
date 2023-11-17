import RPi.GPIO as GPIO
import time

print("Hello, world")

GPIO.setmode(GPIO.BCM)

# RPi GPIO 23 (orange) to L293D Input1
# RPi GPIO 24 (green) to L293D Input2
# RPi GPIO 25 (white) to L293D Enable
Motor1A= 23
Motor2A = 24
Motor1EN = 25

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor1EN, GPIO.OUT)

def forward():
    GPIO.output(Motor1A, GPIO.HIGH) #1
    GPIO.output(Motor2A, GPIO.LOW) #0

def ramp_up():
    pwm.start(80)
    for i in range(80, 110, 10):
        pwm.ChangeDutyCycle(i)
        print("{0}%".format(i))
        time.sleep(5)

pwm = GPIO.PWM(Motor1EN, 1000)

forward()
ramp_up()
pwm.stop()

GPIO.cleanup()