import moisturesensor
import temphumidity

while True:
    moisture = moisturesensor.check_water()
    temperature = temphumidity.check_temperature()
    humidity = temphumidity.check_humidity()

    print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))

    if moisture==0:
        print("No Water Needed")
    else:
        print("Water Needed")

    
    