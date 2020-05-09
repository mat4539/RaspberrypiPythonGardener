import moisturesensor

while True:
    moisture = moisturesensor.callback
    if GPIO.input(moisture):
        print ("Water Detected!")
    else:
        print ("Water Detected!")