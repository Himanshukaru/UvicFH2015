from tkinter import *
from tkinter import ttk
import os

from modules import BatteryRect, FuelRect, EfficiencyBar, Speed

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

CHANGE_GUI_MODE_PIN = 24
REBOOT_PIN = 23

class MainApplication(object):
	root = Tk()
	def __init__(self):
		#self.initializeInterrupts() # TODO marc implement once GPIO PINS are setup
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
		self.root.title("Fuel-Mileage-test")
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
	
	def changeGuiMode(self):
		#TODO Marc, need to cleanup properly, clear all widgets below root
		# Then go to next mode...
		print("Changing Modes")

	def rebootSystem(self):
		# TODO marc: we need to cleanup the gui prior to restarting..
		GPIO.cleanup()
		os.system("sudo reboot")

	def initializeInterrupts(self):
		GPIO.setmode(GPIO.BOARD)
		
		GPIO.setup(REBOOT_PIN, GPIO.IN)
		GPIO.setup(CHANGE_MODE_PIN, GPIO.IN)
		
		GPIO.add_event_detect(REBOOT_PIN, GPIO.FALLING, callback=self.rebootSystem)
		GPIO.add_event_detect(CHANGE_GUI_MODE_PIN, GPIO.FALLING, callback=self.changeGuiMode)
	
if __name__ == "__main__":
	mainApp = MainApplication()
	mainApp.run()
