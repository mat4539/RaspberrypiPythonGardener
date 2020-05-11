import moisturesensor
import temphumidity

while True:
    moisture = moisturesensor.check_water()
    temptemperature = temphumidity.check_temperature()
    humidity = temphumidity.check_humidity()
    print(temptemperature)
    print(humidity)
    
    if moisture==0:
        print("No Water Needed")
    else:
        print("Water Needed")

    
    