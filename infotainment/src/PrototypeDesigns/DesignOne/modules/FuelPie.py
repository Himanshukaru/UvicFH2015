from tkinter import *
from tkinter import ttk
import math
import time

class FuelPie(object):
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas 
           
        self.initializeValues()
        self.createWidget()
        
    def initializeValues(self):
        self.backGroundColor = "#ffffff"
        self.backGroundFillColor = "white"
        
        self.outlineColor = "brown"
        self.fillColor = "brown"
        
        self.frame_rate = 80
        self.center = 120
        self.radius = 110
        self.pieAngle = 90
        
        self.piePositionAngle = 310 # TODO m: need to do this dynamically -> 2*x + 100 = 180 marc you know math
        self.tempCounter = 0 #TODO m: this will be the charge count; for now its a temp counter

    def createWidget(self):
        self.fuelPie = self.canvas.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline=self.outlineColor, fill=self.backGroundFillColor, start=self.piePositionAngle)       
        self.fuelDeltaPie = self.canvas.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline=self.outlineColor, fill=self.fillColor, start=self.piePositionAngle)
        
    def updateFuel(self):
        try:
            self.tempCounter += 1

            if (self.tempCounter > self.pieAngle):
                self.tempCounter = self.pieAngle
            if (self.tempCounter < 0):
                self.tempCounter = 0
                            
            self.canvas.itemconfigure(self.fuelDeltaPie, extent=self.tempCounter)
            self.canvas.update()
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateFuel)