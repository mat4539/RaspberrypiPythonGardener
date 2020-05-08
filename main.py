import moisturesensor

while True:
    moisture = moisturesensor.channel()
    if GPIO.input(moisture):
        print ("Water Detected!")
    else:
        print ("Water Detected!")