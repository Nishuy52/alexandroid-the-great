import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define trig and echo pins for each sensor
sensors = {
    "Ultrasound 1": (10, 0),
    "Ultrasound 2": (9, 5),
    "Ultrasound 3": (11, 6),
}

# Setup GPIO pins
for trig, echo in sensors.values():
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

def get_distance(trig_pin, echo_pin):
    # Ensure trigger is low
    GPIO.output(trig_pin, False)
    time.sleep(0.0002)

    # Send 10us pulse
    GPIO.output(trig_pin, True)
    time.sleep(0.00001)
    GPIO.output(trig_pin, False)

    # Wait for echo to go high
    timeout = time.time() + 0.04
    while GPIO.input(echo_pin) == 0:
        if time.time() > timeout:
            return None
        pulse_start = time.time()

    # Wait for echo to go low
    timeout = time.time() + 0.04
    while GPIO.input(echo_pin) == 1:
        if time.time() > timeout:
            return None
        pulse_end = time.time()

    # Calculate distance
    try:
        duration = pulse_end - pulse_start
        distance = duration * 17150  # Speed of sound ~343 m/s
        return round(distance, 2)
    except:
        return None

try:
    while True:
        for name, (trig, echo) in sensors.items():
            distance = get_distance(trig, echo)
            if distance is not None:
                print(f"{name}: {distance} cm")
            else:
                print(f"{name}: Measurement failed")
        print("-" * 30)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
