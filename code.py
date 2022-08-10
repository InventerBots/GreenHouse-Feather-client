import array
import binascii
import time
import json

import busio
import board
from analogio import AnalogIn
from digitalio import DigitalInOut
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K
# import adafruit_wiznet5k.adafruit_wiznet5k_socket as wizSocket

mac=(98, 76, 19, 12, 9, 253) # 98:76:B6:12:09:ab
host=(192,168,1,220)
port=10004

localIP = ("192.168.1.2")
mask = ("255.255.255.0")
gateway = ("192.168.1.1")
dns = ("8.8.8.8")


cs=DigitalInOut(board.D10)
spi_bus=busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

thermister=AnalogIn(board.A0)

class TempArray:
		def __init__(self, temp1, temp2, temp3) -> None:
				self.temp1 = temp1
				self.temp2 = temp2
				self.temp3 = temp3

		def to_json(self):
				return json.dumps(self)
		
eth=WIZNET5K(spi_bus, cs)
# eth.ifconfig = (localIP, mask, gateway, dns)

#=========> Debug <=========#
# print("Chip Version:", eth.chip)
# print("MAC Address:", [hex(i) for i in eth.mac_address])
# print("IP address:", eth.pretty_ip(eth.ip_address))
#=========> Debug <=========#

# eth.socket_connect(0, host, port)
# print(eth.socket_status(0))

def get_temp(pin) :
		 return ((pin.value*3.3)/65535)

while (True) :
		msg = '25'
		msgwrite = (msg, len(msg))
		json_tempData=TempArray(thermister.value, 0, 0)
		tempRawData=json_tempData.to_json()
		print ("Json incodeing: ", type(tempRawData))

		print("send: ", msgwrite)
		eth.write(host, 1, 25)
		time.sleep(0.5)
# json_tempData=json.loads(json_tempData)
# print(json_tempData)




# tempRaw=json.loads(TempArray)
# print ("Decoded Json: ", tempRaw)

# print(thermister.value)
# print(get_temp(thermister))
# tempRaw=0
# tempHex=bytearray(range(20))
# tempHex = thermister.value()
# print("value: ", tempHex)
# eth.write(0, 65535, tempHex)
time.sleep(0.25)
