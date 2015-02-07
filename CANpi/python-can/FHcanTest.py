import time
import can
can.rc['interface'] = 'socketcan_native'

from can.interfaces.interface import Bus

can_interface = "can0"
def readBus(pBus):
	for message in pBus:
#		print(message)
#		print(message.data[1])
		varTemp = message.data[1]

if __name__ == "__main__":
	bus = Bus(can_interface)
	readBus(bus)
