import busio
import time
import board
from digitalio import DigitalInOut
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as wizSocket
import adafruit_requests as requests

local_IP=str(b'192.168.1.12')
mac=(98, 76, 19, 12, 9, 253) # 98:76:B6:12:09:ab
host=(192,168,1,220)
port=10004

addr='192.168.1.220:10004'

msg="hello"
cs=DigitalInOut(board.D10)
spi_bus=busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

eth=WIZNET5K(spi_bus, cs, None, False, mac, local_IP)
requests.set_socket(wizSocket, eth)

print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))

eth.socket_connect(0, host, port)
