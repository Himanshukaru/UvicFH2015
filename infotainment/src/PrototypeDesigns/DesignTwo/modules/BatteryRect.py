from tkinter import *
from tkinter import ttk
import math
import time

class BatteryRect(object):
    def __init__(self, root):
        self.root = root 
        
        self.initializeValues()
        self.makeMainFrame()
        self.createCanvas()

    def initializeValues(self):
        self.backGroundColor = "#000000"
        self.backGroundFillColor = "green"
        self.outlineColor = "black"
        self.fillColor = "white"
        
        self.frame_rate = 80
        self.x0 = 3
        self.x1 = 60
        self.y0 = 3
        self.y1 = 80
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
        self.currentCharge = self.y1
        
        self.tempCounter = self.currentCharge #TODO m: this will be the charge count; for now its a temp counter
        
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="black")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=2, row=0, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=self.width + 2, height=self.height + 2, background=self.backGroundColor)
        self.canvas.grid(column=0, row=0, sticky=(N,E,W,S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.batteryDeltaobject = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.tempCounter, outline=self.outlineColor, fill=self.fillColor)

    def updateBatteryCharge(self, pCharge=None):
        if pCharge is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.coords(self.batteryDeltaobject, (self.x0, self.y0, self.x1, self.tempCounter))
                self.canvas.update()
            except ValueError:
                pass
        else:
            try:
                self.canvas.coords(self.batteryDeltaobject, (self.x0, self.y0, self.x1, pCharge))
                self.canvas.update()
            except:
                pass #Todo We need to handle these better...
        self.root.after(self.frame_rate,self.updateBatteryCharge)