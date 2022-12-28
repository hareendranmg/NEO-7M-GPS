import smbus
import time

# Open the I2C bus
bus = smbus.SMBus(2)

while(True):
    # Read a single byte from the device at address 0x48
    data = bus.read_byte(0x51)
    # data = bus.read_word_data(0x51, 0x00)
    # Print the data that was read
    print(data)
    time.sleep(0.5)    


