from tkinter import *
from tkinter import ttk
import math
import time

from modules import BatteryRect, FuelRect, EfficiencyBar, Speed

class MainApplication(object):
	root = Tk()
	def __init__(self):
		self.initializeMainWindow()	

		self.battery = BatteryRect.BatteryRect(self.root)
		self.fuel = FuelRect.FuelRect(self.root)
		self.effBar = EfficiencyBar.EfficiencyBar(self.root)
		self.speedHub = Speed.Speed(self.root)
		
	def run(self):
		
		self.battery.updateBatteryCharge()
		self.fuel.updateFuelLevel()
		self.effBar.updateBarPosition()
		self.speedHub.updateSpeed()

		self.root.mainloop()

	def initializeMainWindow(self):
		self.root.configure(bg="#000000")
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
