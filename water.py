import time
import RPi.GPIO as GPIO

def watering(to_water):

    # Send POST to update database with time
    dict = [{
            "id": 1,
            "watering": "started",
            "expectedTimeInSeconds": 10,
	    "status": "started"
            }]

    # Start async job in background

    pin = 21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)
    time.sleep(to_water)
    GPIO.output(pin, False)

    return 200


def getStatus():

    # GET to retrieve when
    get = {
        "status": "started"
    }
    dict = [{
        "id": 1,
        "status": get['status'],
        "wateredLast": 300
    }]
    return dict
