import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 20

humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

def check_humidity():
    return humidity
    time.sleep(3)


def check_temperature():
    return temperature
    time.sleep(3)
