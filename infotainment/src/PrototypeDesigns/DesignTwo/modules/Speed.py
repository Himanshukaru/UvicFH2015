from tkinter import *
from tkinter import ttk
import math
import time

class Speed(object):
    def __init__(self, root):
        self.root = root
                
        self.initializeValues()
        self.makeMainFrame()
        self.makeCanvas()
        
    def initializeValues(self):
        self.speedFont = "helvetica 30 bold"
        self.kphFont = "helvetica 10 bold"
        self.textColor = "white"
        
        self.backGroundColor = "#000000"
        self.outlineColor = "black"
        self.backGroundFillColor = "blue"
        self.fillColor = "black"
        
        self.canvasWidth = 120 + 90 + 50
        self.center = 100
        self.radius = 90
        
        self.frame_rate = 80
        self.centerX = 150
        self.centerY = 80
        self.maxSpeed = 280
        
        self.speed = ""
        
        self.tempCounter = 0 #TODO m: this will be the charge count; for now its a temp counter
        
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="black")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=1, row=1, sticky=(N, E, W, S))
        
    def makeCanvas(self):
        self.canvas = Canvas(self.mainFrame, background=self.backGroundColor, width=self.canvasWidth, height=self.canvasWidth, bg="#000000")
        self.canvas.grid(column=0, row=1, sticky=(N,E,W,S))
        
        self.hubCircle = self.canvas.create_oval(self.center-self.radius + 50, self.center-self.radius, self.center+self.radius + 50, self.center+self.radius, outline=self.outlineColor, fill=self.backGroundFillColor)
        self.speedText = self.canvas.create_text(self.centerX, self.centerY, text=self.speed, fill=self.textColor, font=self.speedFont)
        self.kphLabel = self.canvas.create_text(self.centerX, self.centerY + 20, text="kph", fill=self.textColor, font=self.kphFont)

    def updateSpeed(self, pSpeed):
        if pSpeed is None:
            try:
                self.tempCounter += 1
    
                if (self.tempCounter > self.maxSpeed):
                    self.tempCounter = self.maxSpeed
                if (self.tempCounter < 0):
                    self.tempCounter = 0
                
                self.speed = str(self.tempCounter)
                #self.canvas.itemconfigure(self.speedText, text=self.speed)
    
                #self.canvas.update()                                
            except ValueError:
                pass
        
        try:
            self.canvas.itemconfigure(self.speedText, text=str(pSpeed))
            self.canvas.update()                                
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateSpeed)