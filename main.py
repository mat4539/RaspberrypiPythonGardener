import moisturesensor

while True:
    moisture = moisturesensor.check_water()
    print(moisture)