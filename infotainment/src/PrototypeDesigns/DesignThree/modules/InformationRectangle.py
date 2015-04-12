from tkinter import *
from tkinter import ttk
import math
import time

class InformationRectangle(object):
    def __init__(self, root):
        self.root = root 
        
        self.initializeValues()
        self.makeMainFrame()
        self.createCanvas()

    def initializeValues(self): 
        self.initliazeWidgetValues()
        self.initializeCanvasSize()
        self.initializeCanvasSize()
        self.initializeFontSizeColor()
        self.initializeOffsets()
        self.tempCounter = 100
    
    def initliazeWidgetValues(self):
        self.speed = 0
        self.fuel = 0
        self.charge = 0
        self.rpm = 0
        self.coolant = 0
        
    def initializeCanvasSize(self):
        self.WINDOW_BUFFER = 2
        
        self.frame_rate = 80
        self.x0 = 0 + self.WINDOW_BUFFER
        self.x1 = 990
        self.y0 = 0 + self.WINDOW_BUFFER
        self.y1 = 80
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
    def initializeFontSizeColor(self):
        self.backGroundColor = "#000000"
        self.backGroundFillColor = "black"
        self.outlineColor = "black"
        self.fillColor = "white"
        
        self.speedFont = "helvetica 30 bold"
        self.kphFont = "helvetica 10 bold"
        self.textColor = "white"
        self.rpmLabelFont = "helvetica 10 bold"
        self.rpmTextFont = "helvetica 30 bold"
        self.coolantLabelFont = "helvetica 10 bold"
        self.coolantTextFont = "helvetica 30 bold"
        
        
    def initializeOffsets(self):
        
        self.speedLabelOffsetX = 60
        self.speedLabelOffsetY = 10
        self.speedOffsetX = 20
        self.speedOffsetY = 10
        
        self.rpmLabelOffsetX = 100
        self.rpmLabelOffsetY = 50
        self.rpmOffsetX = 45
        self.rpmOffsetY = 50

        self.fuelLabelOffsetX = 200
        self.fuelLabelOffsetY = 50
        self.fuelOffsetX = 280
        self.fuelOffsetY = 50
        
        self.chargeLabelOffsetX = 200
        self.chargeLabelOffsetY = 10        
        self.chargeOffsetX = 280
        self.chargeOffsetY = 10

        self.coolantLabelOffsetX = 380
        self.coolantLabelOffsetY = 10
        self.coolantTempOffsetX = 340
        self.coolantTempOffsetY = 10
                      
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="black")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=1, row=1, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        
    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=self.width + self.WINDOW_BUFFER, height=self.height, background=self.backGroundColor)
        self.canvas.grid(column=0, row=0, sticky=(N, E, W, S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.speedText = self.canvas.create_text(self.x0 + self.speedOffsetX, self.y0 + self.speedOffsetY, text=self.speed, fill=self.textColor, font=self.speedFont)
        self.speedLabel = self.canvas.create_text(self.x0 + self.speedLabelOffsetX, self.y0 + self.speedLabelOffsetY, text="KPH", fill=self.textColor, font=self.kphFont)
        
        self.fuelText = self.canvas.create_text(self.x0 + self.fuelOffsetX, self.y0 + self.fuelOffsetY, text=self.fuel, fill=self.textColor, font=self.speedFont)
        self.fuelLabel = self.canvas.create_text(self.x0 + self.fuelLabelOffsetX, self.y0 + self.fuelLabelOffsetY, text="Fuel % Left:", fill=self.textColor, font=self.kphFont)
        
        self.chargeText = self.canvas.create_text(self.x0 + self.chargeOffsetX, self.y0 + self.chargeOffsetY, text=self.charge, fill=self.textColor, font=self.speedFont)
        self.chargeLabel = self.canvas.create_text(self.x0 + self.chargeLabelOffsetX, self.y0 + self.chargeLabelOffsetY, text="Charge % Left:", fill=self.textColor, font=self.kphFont)
        
        self.rpmText = self.canvas.create_text(self.x0 + self.rpmOffsetX, self.y0 + self.rpmOffsetY, text=self.rpm, fill=self.textColor, font=self.rpmTextFont)
        self.rpmLabel = self.canvas.create_text(self.x0 + self.rpmLabelOffsetX, self.y0 + self.rpmLabelOffsetY, text="RPM", fill=self.textColor, font=self.rpmLabelFont)
        
        self.coolantText = self.canvas.create_text(self.x0 + self.coolantTempOffsetX, self.y0 + self.coolantTempOffsetY, text=self.coolant, fill=self.textColor, font=self.coolantTextFont)
        self.coolantLabel = self.canvas.create_text(self.x0 + self.coolantLabelOffsetX, self.y0 + self.coolantLabelOffsetY, text="CLT", fill=self.textColor, font=self.coolantLabelFont)
        
    def updateCoolantRectangle(self, pCoolant=None):
        if pCoolant is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.coolantText, text=str(self.tempCounter))
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.coolant = pCoolant
            self.canvas.itemconfigure(self.coolantText, text=str(pCoolant))
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateCoolantRectangle)
        
    def updateFuelRectangle(self, pFuel=None):
        if pFuel is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.fuelText, text=str(self.tempCounter))
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.fuel = pFuel
            self.canvas.itemconfigure(self.fuelText, text=str(pFuel))
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateFuelRectangle)

    def updateSpeedRectangle(self, pSpeed=None):
        if pSpeed is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.speedText, text=str(self.tempCounter))
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.speed = pSpeed
            self.canvas.itemconfigure(self.speedText, text=str(pSpeed))
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateSpeedRectangle)

    def updateRPMRectangle(self, pRPM=None):
        if pRPM is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.rpmText, text=str(self.tempCounter * 1000))
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.canvas.itemconfigure(self.rpmText, text=str(pRPM))
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateRPMRectangle)
        
    def updateChargeRectangle(self, pCharge=None):
        if pCharge is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.chargeText, text=str(self.tempCounter))
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.charge = pCharge
            self.canvas.itemconfigure(self.chargeText, text=str(pCharge))
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateChargeRectangle)
    
    def updateWarnings(self):
        print("Warnings, yo")

#===============================================================================
# if __name__ == "__main__":
#     root = Tk()
#     testRect = InformationRectangle(root)
#     
#     testRect.updateFuelRectangle()
#     testRect.updateSpeedRectangle()
#     testRect.updateRPMRectangle()
#     testRect.updateChargeRectangle()
#     testRect.updateCoolantRectangle()
#     
#     root.mainloop()
#===============================================================================
