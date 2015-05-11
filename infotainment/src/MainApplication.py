from tkinter import *
from tkinter import ttk
import os
from random import randint
import CAN_Main
# Width: 1232
# Height: 768
from modules import BatteryRect, FuelRect, EfficiencyBar, InformationRectangle, WarningRectangle

try:
    import RPi.GPIO as GPIO
except ImportError:
    # TODO Marc, write a shell script to re-run the main app as sudo, os.system("ps -ef | grep MainApplication.py | grep "pid" | kill; sudo MainApplication.py")
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

CHANGE_GUI_MODE_PIN = 21
REBOOT_PIN = 20

class MainApplication(object):
    root = Tk()
    frame_rate = 40
    def __init__(self):
        # self.initializeInterrupts() # TODO marc implement once GPIO PINS are setup
        self.initializeMainWindow()	

        self.battery = BatteryRect.BatteryRect(self.root)
        self.fuel = FuelRect.FuelRect(self.root)
        self.infoRect = InformationRectangle.InformationRectangle(self.root)
        self.warnRect = WarningRectangle.WarningRectangle(self.root)

        self.canMain = CAN_Main.CAN_Main()
        self.canMain.initializeInstances()
        		
    def run(self):
        self.pollBus()
        self.checkForUpdates()
        self.root.mainloop()

    def initializeMainWindow(self):
        self.root.configure(bg="white")
        self.root.title("Fuel-Mileage-test")
        self.root.attributes("-fullscreen", True)
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

    def pollBus(self):
        self.canMain.pollBus()
        self.root.after(self.frame_rate, self.pollBus)
	
    
    def checkForUpdates(self):
        if self.canMain.update_vehicle_speed:
            self.infoRect.updateSpeedRectangle(self.canMain.current_vehicle_speed)
            self.canMain.update_vehicle_speed = False

        if self.canMain.update_engine_RPM:
            self.infoRect.updateRPMRectangle(self.canMain.current_engine_RPM)
            self.canMain.update_engine_RPM = False
              
        if self.canMain.update_throttle_percent:
            self.infoRect.updateEngineTPS(self.canMain.current_throttle_percent)
            self.canMain.update_throttle_percent = False
              
        if self.canMain.update_engine_coolant_temp:
            self.infoRect.updateCoolantRectangle(self.canMain.current_engine_coolant_temp)
            self.canMain.update_engine_coolant_temp = False

        if self.canMain.update_ess_soc:
            self.infoRect.updateChargeRectangle(self.canMain.current_ess_soc)
            self.battery.updateBatteryCharge(self.canMain.current_ess_soc)
            self.canMain.update_ess_soc = False
            
#        TODO Need to implement can interface for fuel
#         if self.canMain.update_fuel_level:
#             
#        TODO Need to implement can interface for motor TPS
         
        self.root.after(self.frame_rate, self.checkForUpdates)
	
    def changeGuiMode(self, channel):
        # TODO Marc, need to cleanup properly, clear all widgets below root
        # Then go to next mode...
        print("Changing Modes")

    def rebootSystem(self, channel):
        # TODO marc: we need to cleanup the gui prior to restarting..
        GPIO.cleanup()
        # os.system("sudo reboot")

    def initializeInterrupts(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(REBOOT_PIN, GPIO.IN)
        GPIO.setup(CHANGE_MODE_PIN, GPIO.IN)
        
        GPIO.add_event_detect(REBOOT_PIN, GPIO.FALLING, callback=self.rebootSystem)
        GPIO.add_event_detect(CHANGE_GUI_MODE_PIN, GPIO.FALLING, callback=self.changeGuiMode)
	
if __name__ == "__main__":
    mainApp = MainApplication()
    mainApp.run()
