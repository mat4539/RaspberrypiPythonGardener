import moisturesensor

while True:
    moisture = moisturesensor.check_water()
    print(moisture)
    if moisture==0:
        print("No Water Needed")
    else:
        print("Water Needed")
    