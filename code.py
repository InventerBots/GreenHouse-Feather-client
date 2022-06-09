# from socket import AF_INET, SOCK_STREAM
import busio
import time
import board
from digitalio import DigitalInOut
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
import adafruit_wiznet5k.adafruit_wiznet5k_socket as wizSocket
# import socketpool as pool

local_IP=(192,168,1,12)
mac=('98','76','B6','12','o9','ab')
host=(192,168,1,220)
port=10004
msg="hello"
cs=DigitalInOut(board.D10)
spi_bus=busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# eth=WIZNET5K(spi_bus, cs,reset=None, is_dhcp=False,mac=mac, hostname=local_IP)



# print("Local IP: ", eth.pretty_ip(eth.ip_address()))
# print("Local MAC: ", eth.pretty_mac(eth.mac_address()))
# eth.socket_open(port)
# eth.socket_connect([host, port])