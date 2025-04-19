import RPi.GPIO as GPIO
import time

# Pin definitions (BCM mode)
s2 = 23
s3 = 24
signal = 25
NUM_CYCLES = 100  # Adjust as needed

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Ensure the signal pin is set as input
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    print("Color sensor initialized. Reading will start...\n")

def count_pulses(pin, num_cycles, timeout=2.0):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    count = 0
    start_time = time.time()
    while count < num_cycles:
        try:
            if GPIO.wait_for_edge(pin, GPIO.FALLING, timeout=int(timeout * 1000)):  # Timeout in ms
                count += 1
            else:
                print(f"Timeout waiting for pulse {count + 1}/{num_cycles}")
                break
        except Exception as e:
            print(f"Error during pulse counting: {e}")
            break
    duration = time.time() - start_time
    return duration if count == num_cycles else None

def loop():
    while True:
        try:
            # RED
            GPIO.output(s2, GPIO.LOW)
            GPIO.output(s3, GPIO.LOW)
            time.sleep(1)
            duration = count_pulses(signal, NUM_CYCLES)
            if duration:
                red = NUM_CYCLES / duration
                print(f"Red   frequency: {red:.2f} Hz")
            else:
                red = 0
                print("Red reading timed out.")
            # GREEN
            GPIO.output(s2, GPIO.HIGH)
            GPIO.output(s3, GPIO.HIGH)
            time.sleep(1)
            duration = count_pulses(signal, NUM_CYCLES)
            if duration:
                green = NUM_CYCLES / duration
                print(f"Green frequency: {green:.2f} Hz")
            else:
                green = 0
                print("Green reading timed out.")
                
            # BLUE
            GPIO.output(s2, GPIO.LOW)
            GPIO.output(s3, GPIO.HIGH)
            time.sleep(1)
            duration = count_pulses(signal, NUM_CYCLES)
            if duration:
                blue = NUM_CYCLES / duration
                print(f"Blue  frequency: {blue:.2f} Hz")
            else:
                blue = 0
                print("Blue reading timed out.")

            

            print("-" * 40)
            time.sleep(1)

        except KeyboardInterrupt:
            break

def endprogram():
    GPIO.cleanup()
    print("GPIO cleaned up. Exiting...")

if __name__ == '__main__':
    setup()
    try:
        loop()
    finally:
        endprogram()
