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
        self.backGroundColor = "white"
        self.backGroundFillColor = "green"
        self.outlineColor = "green"
        self.fillColor = "white"
        self.font = "helvetica 30 bold"
        
        self.frame_rate = 40
        self.x0 = 0
        self.x1 = 140
        self.y0 = 0
        self.y1 = 668
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
        self.currentCharge = 0
        
        self.tempCounter = self.currentCharge  # TODO m: this will be the charge count; for now its a temp counter
        
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="black")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=2, row=1, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=self.width + 2, height=self.height + 2, background=self.backGroundColor)
        self.canvas.grid(column=0, row=0, sticky=(N, E, W, S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.batteryDeltaobject = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.tempCounter, outline=self.outlineColor, fill=self.fillColor)
        self.chargeText = self.canvas.create_text(self.width/2, self.height/2, text=self.currentCharge, fill="black", font=self.font)

    def updateBatteryCharge(self, pCharge):
        if pCharge is None:
            try:
                self.tempCounter += 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.coords(self.batteryDeltaobject, (self.x0, self.y0, self.x1, self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            displayVar = self.height - ((pCharge/100)*self.height)
            self.canvas.coords(self.batteryDeltaobject, (self.x0, self.y0, self.x1, displayVar))
            self.canvas.itemconfigure(self.chargeText, text=str(pCharge) + " %")
            self.canvas.update()
        except ValueError:
            pass  # Todo We need to handle these better...
        #self.root.after(self.frame_rate, self.updateBatteryCharge)
