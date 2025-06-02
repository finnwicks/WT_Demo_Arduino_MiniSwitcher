import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the relay is connected
RELAY_PIN = 17

# Set up the relay pin
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Function to open the solenoid valve
def open_solenoid():
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Activate the relay
    print("Solenoid Valve Opened")

# Function to close the solenoid valve
def close_solenoid():
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Deactivate the relay
    print("Solenoid Valve Closed")

def main():
    try:
        while True:
            # Open the solenoid valve for 5 seconds
            open_solenoid()
            time.sleep(0.1)  # Keep it open for 5 seconds
            close_solenoid()
            time.sleep(1)  # Wait 1 second before opening again or adjust as needed

    except KeyboardInterrupt:
        print("Program interrupted.")

    finally:
        close_solenoid()  # Ensure solenoid is closed on exit
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()