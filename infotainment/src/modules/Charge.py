from tkinter import *
from tkinter import ttk
import math
import time

class Charge(object):
    def __init__(self, root, canvas):
        self.root = root 
        self.canvas = canvas
        
        self.initializeValues()
        self.createWidget()

    def initializeValues(self):
        self.backGroundColor = "#ffffff"
        self.backGroundFillColor = "green"
        self.outlineColor = "green"
        self.fillColor = "white"
        
        self.frame_rate = 80
        self.center = 120
        self.radius = 110
        self.pieAngle = 90
        
        self.piePositionAngle = 140
        self.tempCounter = self.pieAngle #TODO m: this will be the charge count; for now its a temp counter

    def createWidget(self):
        self.chargePie = self.canvas.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline=self.outlineColor, fill=self.backGroundFillColor, start=self.piePositionAngle)
        
        self.chargeDeltaPie = self.canvas.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline=self.outlineColor, fill=self.fillColor, start=self.piePositionAngle)

    def updateCharge(self):
        try:
            self.tempCounter -= 1

            if (self.tempCounter > self.pieAngle):
                self.tempCounter = self.pieAngle
            if (self.tempCounter < 0):
                self.tempCounter = 0
                            
            self.canvas.itemconfigure(self.chargeDeltaPie, extent=self.tempCounter)
            self.canvas.update()
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateCharge)