import time
import can
can.rc['interface'] = 'socketcan_native'

from can.interfaces.interface import Bus

can_interface = "can0"

class CanMessageRead(object):
	bus = Bus(can_interface)
	def __init__(self):
		self.id = 0
		self.currentDistance = 0	
		self.prevDistance = 0

	def readBus(self):
		try:	
			msg = self.bus.recv()
			self.id = msg.data[0]
			self.prevDistance = self.currentDistance
			self.currentDistance = msg.data[1]
		except:
			print("TODO m: We need to catch this, yo")

