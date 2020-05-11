import moisturesensor

while True:
    moisture = moisturesensor.callback()
    print(moisture)
