import array
import time

import busio
import board
from analogio import AnalogIn
from digitalio import DigitalInOut
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as wizSocket
import adafruit_requests as requests

mac=(98, 76, 19, 12, 9, 253) # 98:76:B6:12:09:ab
host=(192,168,1,220)
port=10004

msg="hello"

cs=DigitalInOut(board.D10)
spi_bus=busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

thermister=AnalogIn(board.A0)

eth=WIZNET5K(spi_bus, cs)
requests.set_socket(wizSocket, eth)

#=========> Debug <=========#
print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("IP address:", eth.pretty_ip(eth.ip_address))
#=========> Debug <=========#
eth.socket_connect(0, host, port)

def get_temp(pin) :
        return ((pin.value*3.3)/65535)

while True:
    print(thermister.value)
    print(get_temp(thermister))
    tempRaw=0
    print("bin ", bin(thermister.value))
#     eth.socket_write(0, bin(get_temp(thermister)))
    time.sleep(0.25)
