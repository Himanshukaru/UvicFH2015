from tkinter import *
from tkinter import ttk
import math
import time

INNEFICIENT_DRIVING_LIMIT = 200
OVER_EFFICIENT_DRIVING_LIMIT = 100

class EfficiencyBar(object):
    def __init__(self, root):
        self.root = root 
        
        self.initializeValues()
        self.makeMainFrame()
        self.createCanvas()

    def initializeValues(self):
        self.backGroundColor = "#000000"
        self.backGroundFillColor = "black"
        self.outlineColor = "white"
        self.fillColor = "blue"
        
        self.testingChangeBool = False
        
        self.frame_rate = 80
        self.x0 = 3
        self.x1 = 300
        self.y0 = 3
        self.y1 = 15
        
        self.centerX = (self.x1 + self.x0)/2
        self.centerY = (self.y1 + self.y0)/2
        
        self.efficiencyBarPositionX = self.centerX
        
        self.tempCounter = self.efficiencyBarPositionX #TODO m: this will be the charge count; for now its a temp counter
        
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="black")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=1, row=0, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=self.x1, height=self.y1, background=self.backGroundColor)
        self.canvas.grid(column=0, row=0, sticky=(N,E,W,S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.efficiencyBar = self.canvas.create_rectangle(self.efficiencyBarPositionX, self.y0, self.tempCounter, self.y1, outline=self.outlineColor, fill=self.fillColor)

    def updateBarPosition(self):
        try:
            if (self.testingChangeBool):
                self.tempCounter -= 2
            else:
                self.tempCounter += 2
                
            if (self.tempCounter > INNEFICIENT_DRIVING_LIMIT):
                self.canvas.itemconfigure(self.efficiencyBar, fill="red")
            elif (self.tempCounter < OVER_EFFICIENT_DRIVING_LIMIT):
                self.canvas.itemconfigure(self.efficiencyBar, fill="yellow")
            elif (self.tempCounter > OVER_EFFICIENT_DRIVING_LIMIT and self.tempCounter < INNEFICIENT_DRIVING_LIMIT):
                self.canvas.itemconfigure(self.efficiencyBar, fill="blue")
            
            if (self.tempCounter >= self.x1):
                self.tempCounter = self.x1
                self.testingChangeBool = True
            if (self.tempCounter <= self.x0):
                self.tempCounter = self.x0
                self.testingChangeBool = False
            
            self.canvas.coords(self.efficiencyBar, (self.efficiencyBarPositionX, self.y0, self.tempCounter, self.y1))
            self.canvas.update()
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateBarPosition)