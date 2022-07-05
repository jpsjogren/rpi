import time
import RPi.GPIO as GPIO

def watering(to_water, pin):


    # Start async job in background
    print(pin)
    if pin is None:
        return 400
    else:
        pin = pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(to_water)
    GPIO.output(pin, False)
    GPIO.cleanup()

    return 201
