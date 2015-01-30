from tkinter import *
from tkinter import ttk
import math
import time

from modules import FuelGauge, ChargeGauge, Speedometer

class MainApplication(object):
	root = Tk()
	def __init__(self):
		self.initializeMainWindow()	

		self.fuelGauge = FuelGauge.FuelGauge(self.root)
		self.chargeGauge = ChargeGauge.ChargeGauge(self.root)
		self.speedometer = Speedometer.Speedometer(self.root)

	def run(self):
		
		self.fuelGauge.rotateLine()
		self.chargeGauge.rotateLine()
		self.speedometer.rotateLine()

		self.root.mainloop()

	def initializeMainWindow(self):
		self.root.title("Fuel-Milage-test")
		self.root.attributes("-fullscreen",True)
		self.root.bind()
		self.state = False
		self.root.bind("<F11>", self.toggle_fullscreen)
		self.root.bind("<Escape>", self.end_fullscreen)

	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.root.attributes("-fullscreen", self.state)
		return "break"

	def end_fullscreen(self, event=None):
		self.state = False
		self.root.attributes("-fullscreen", False)
		return "break"
	
if __name__ == "__main__":
	mainApp = MainApplication()
	mainApp.run()
