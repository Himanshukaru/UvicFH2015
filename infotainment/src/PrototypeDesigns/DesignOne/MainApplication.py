from tkinter import *
from tkinter import ttk
import math
import time

from modules import ChargePie, FuelPie, Speed

class MainApplication(object):
    root = Tk()
    def __init__(self):
        self.initializeMainWindow()
        self.initializeValues()

        self.makeMainFrame()
        self.makeCanvas()
        
        self.fuel = FuelPie.FuelPie(self.root, self.hubPie)
        self.charge = ChargePie.ChargePie(self.root, self.hubPie)
        self.hubPie.lift(self.hubCircle)
        self.speed = Speed.Speed(self.root, self.hubPie)
        
    def run(self):
        self.fuel.updateFuel()
        self.charge.updateCharge()
        self.speed.updateSpeed()
        self.root.mainloop()
    
    def initializeValues(self):
        self.backGroundColor = "#ffffff"
        self.outlineColor = "black"
        self.backGroundFillColor = "black"
        self.fillColor = "black"
        
        self.canvasWidth = 500
        self.center = 120
        self.radius = 90
    
    def makeMainFrame(self):
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainFrame.grid(column=3, row=0, columnspan=3, rowspan=3, sticky=(N, E, W, S))
        
    def makeCanvas(self):
        self.hubPie = Canvas(self.mainFrame, background=self.backGroundColor, width=self.canvasWidth, height=self.canvasWidth)
        self.hubPie.grid(column=3, row=0, sticky=(N,E,W,S))
        self.hubCircle = self.hubPie.create_oval(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, outline=self.outlineColor, fill=self.backGroundFillColor)
        
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