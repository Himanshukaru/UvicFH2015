from tkinter import *
from tkinter import ttk
import math
import time

class Speed(object):
    def __init__(self, root, canvas):
        self.root = root 
        self.canvas = canvas
        
        self.initializeValues()
        self.createWidget()

    def initializeValues(self):
        self.speedFont = "helvetica 30 bold"
        self.kphFont = "helvetica 10 bold"
        self.textColor = "white"
        
        self.backGroundColor = "#ffffff"
        self.outlineColor = "black"
        self.backGroundFillColor = "black"
        self.fillColor = "black"
        
        self.canvasWidth = 500
        self.center = 120
        self.radius = 90
        
        self.frame_rate = 80
        self.centerX = 120
        self.centerY = 100
        self.maxSpeed = 280
        
        self.speed = ""
        
        self.tempCounter = 0 #TODO m: this will be the charge count; for now its a temp counter

    def createWidget(self):
        self.speedText = self.canvas.create_text(self.centerX, self.centerY, text=self.speed, fill=self.textColor, font=self.speedFont)
        self.kphLabel = self.canvas.create_text(self.centerX, self.centerY + 20, text="kph", fill=self.textColor, font=self.kphFont)

    def updateSpeed(self, pSpeed=None):
        if pSpeed is None:
            try:
                self.tempCounter += 1
    
                if (self.tempCounter > self.maxSpeed):
                    self.tempCounter = self.maxSpeed
                if (self.tempCounter < 0):
                    self.tempCounter = 0
                
                self.speed = str(self.tempCounter)
                self.canvas.itemconfigure(self.speedText, text=self.speed)
    
                self.canvas.update()                                
            except ValueError:
                pass
        else:
            self.canvas.itemconfigure(self.speedText, text=str(pSpeed))
            self.canvas.update()
        self.root.after(self.frame_rate,self.updateSpeed)