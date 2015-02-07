from tkinter import *
from tkinter import ttk

# Custom Class import
import CanMessageRead

#CAN imports
import can
can.rc['interface'] = 'socketcan_native'
from can.interfaces.interface import Bus
can_interface = "can0"

class DistanceGui(object):
	root = Tk()
	def __init__(self):
		self.currentDistance = StringVar()
		self.currentDistance.set(0)
		self.frame_rate = 80
		self.initializeMainWindow()
		self.makeMainFrame()
		self.makeCanvas()
		
		self.canMsg = CanMessageRead.CanMessageRead()

	def initializeMainWindow(self):
		self.root.title("FH CAN TEST")
		self.root.attributes("-fullscreen", True)
		self.root.bind()
		self.state = False
	
	def makeMainFrame(self):
		self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe.grid(column=0, row=0, columnspan=1, rowspan=2, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1) 

	def makeCanvas(self):
		self.distanceLabel = ttk.Label(self.mainframe, textvariable=self.currentDistance, width=3, font="Helvetica 36 bold")
		self.distanceLabel.grid(column=0, row=1, sticky=(E))
		
		self.distanceTextLabel = ttk.Label(self.mainframe, text="DISTANCE (cm)", font="Helvetica 10 bold")
		self.distanceTextLabel.grid(column=1, row=1, sticky=(W))

	def increaseNum(self, pDistance):
		try:
			self.currentDistance.set(pDistance)
		except ValueError:
			pass
	
	def pollBus(self):
		self.canMsg.readBus()
		if self.canMsg.prevDistance != self.canMsg.currentDistance:
			self.increaseNum(self.canMsg.currentDistance)
		else:
			pass
		self.root.after(self.frame_rate, self.pollBus)
	
	def run(self):
		#this is where the magic is going to happen
		self.pollBus()	
		self.root.mainloop()

if __name__ == "__main__":
	distGui = DistanceGui()
	distGui.run()	
