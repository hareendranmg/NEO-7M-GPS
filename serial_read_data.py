import serial
import time
import sys

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)

    while True:
        # ser.write(b'hello')
        data = ser.readline()
        print(data)
        time.sleep(0.5)
except KeyboardInterrupt:
    print('closing...')
    ser.close()
    sys.exit(0)
