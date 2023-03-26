print("project started")
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# for ultrasonic sensor use in front
GPIO_ECHO_US1 = 13

GPIO_TRIG_US1 = 11
GPIO.setup(GPIO_ECHO_US1, GPIO.IN)

GPIO.setup(GPIO_TRIG_US1, GPIO.OUT)
GPIO.output(GPIO_TRIG_US1, GPIO.LOW)

time.sleep(2)
GPIO.output(GPIO_TRIG_US1, GPIO.HIGH)

time.sleep(0.00001)

GPIO.output(GPIO_TRIG_US1, GPIO.LOW)

while GPIO.input(GPIO_ECHO_US1) == 0:
    start_time = time.time()

while GPIO.input(GPIO_ECHO_US1) == 1:
    Bounce_back_time = time.time()

pulse_duration = Bounce_back_time - start_time

distance_front = round(pulse_duration * 17150, 2)

print ("Obstacle distance in front : ",distance_front,"cm")
if (distance_front < 50 ):
    print("alert object near in front")

# for ultrasonic sensor use in left
GPIO_ECHO_US2 = 12

GPIO_TRIG_US2 = 10
GPIO.setup(GPIO_ECHO_US2, GPIO.IN)
GPIO.setup(GPIO_TRIG_US2, GPIO.OUT)
GPIO.output(GPIO_TRIG_US2, GPIO.LOW)

time.sleep(2)
GPIO.output(GPIO_TRIG_US2, GPIO.HIGH)

time.sleep(0.00001)

GPIO.output(GPIO_TRIG_US2, GPIO.LOW)

while GPIO.input(GPIO_ECHO_US2) == 0:
    start_time = time.time()

while GPIO.input(GPIO_ECHO_US2) == 1:
    Bounce_back_time = time.time()

pulse_duration = Bounce_back_time - start_time

distance_left = round(pulse_duration * 17150, 2)

print ("Obstacle distance in left : ",distance_left,"cm")
if (distance_left < 50 ):
    print("alert object near in left")

# for ultrasonic sensor use in right
GPIO_ECHO_US3 = 14

GPIO_TRIG_US3 = 9
GPIO.setup(GPIO_ECHO_US3, GPIO.IN)

GPIO.setup(GPIO_TRIG_US3, GPIO.OUT)
GPIO.output(GPIO_TRIG_US3, GPIO.LOW)

time.sleep(2)
GPIO.output(GPIO_TRIG_US3, GPIO.HIGH)

time.sleep(0.00001)

GPIO.output(GPIO_TRIG_US3, GPIO.LOW)

while GPIO.input(GPIO_ECHO_US3) == 0:
    start_time = time.time()

while GPIO.input(GPIO_ECHO_US3) == 1:
    Bounce_back_time = time.time()

pulse_duration = Bounce_back_time - start_time

distance_right = round(pulse_duration * 17150, 2)

print ("Obstacle distance in right : ",distance_right,"cm")
if (distance_right < 50 ):
    print("alert object near in right")