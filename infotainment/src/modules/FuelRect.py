from tkinter import *
from tkinter import ttk
import math
import time

class FuelRect(object):
    def __init__(self, root):
        self.root = root 
        self.initializeMainWindow()
        
        self.initializeValues()
        self.makeMainFrame()
        self.createCanvas()
        
    def initializeMainWindow(self):
        self.root.title("Fuel-Milage-test")
        self.root.attributes("-fullscreen",True)
        self.root.bind()
        self.state = False
        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<Escape>", self.end_fullscreen)

    def initializeValues(self):
        self.backGroundColor = "#ffffff"
        self.backGroundFillColor = "brown"
        self.outlineColor = "black"
        self.fillColor = "white"
        
        self.frame_rate = 80
        self.x0 = 1380
        self.x1 = 1437
        self.y0 = 3
        self.y1 = 80
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
        self.currentFuel = self.y1
        
        self.tempCounter = self.currentFuel #TODO m: this will be the charge count; for now its a temp counter
        
    def makeMainFrame(self):
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainFrame.grid(column=2, row=0, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)

    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=1440, height=self.height, background=self.backGroundColor)
        self.canvas.grid(column=2, row=0, sticky=(N,E,W,S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.fuelDeltaobject = self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.tempCounter, outline=self.outlineColor, fill=self.fillColor)

    def updateFuelLevel(self):
        try:
            self.tempCounter -= 1

            if (self.tempCounter >= self.y1):
                self.tempCounter = self.y1
            if (self.tempCounter <= self.y0):
                self.tempCounter = self.y0
            
            self.canvas.coords(self.fuelDeltaobject, (self.x0, self.y0, self.x1, self.tempCounter))
            self.canvas.update()
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateFuelLevel)
        
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
    root = Tk()
    testFuel = FuelRect(root)
    testFuel.updateFuelLevel()
    root.mainloop()