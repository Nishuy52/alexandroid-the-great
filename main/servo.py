import RPi.GPIO as GPIO
import time

# GPIO pin setup
servo1_pin = 17  # GPIO17
servo2_pin = 27  # GPIO27

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1_pin, GPIO.OUT)
GPIO.setup(servo2_pin, GPIO.OUT)

# Set frequency to 50Hz (standard for servos)
pwm1 = GPIO.PWM(servo1_pin, 50)
pwm2 = GPIO.PWM(servo2_pin, 50)

# Start PWM at neutral positions
pwm1.start(7)   # Neutral for Servo 1
pwm2.start(9)   # Neutral for Servo 2
time.sleep(1)

print("Enter 'o1' to open Servo 1, 'c1' to close Servo 1,")
print("      'o2' to open Servo 2, 'c2' to close Servo 2,")
print("      or 'exit' to quit.")

try:
    while True:
        command = input("Command: ").strip().lower()

        if command == "o1":
            pwm1.ChangeDutyCycle(12.5)  # Open Servo 1
            print("Servo 1 opened")
        elif command == "c1":
            pwm1.ChangeDutyCycle(7)     # Close Servo 1
            print("Servo 1 closed")
        elif command == "o2":
            pwm2.ChangeDutyCycle(2.5)   # Open Servo 2
            print("Servo 2 opened")
        elif command == "c2":
            pwm2.ChangeDutyCycle(9)     # Close Servo 2
            print("Servo 2 closed")
        elif command == "exit":
            break
        else:
            print("Invalid command. Try again.")

        time.sleep(0.5)  # Wait a bit to let servo move

finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()
    print("Cleaned up and exiting.")
