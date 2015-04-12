from tkinter import *
from tkinter import ttk
import math
import time

class WarningRectangle(object):
    def __init__(self, root):
        self.root = root 
        
        self.initializeValues()
        self.makeMainFrame()
        self.createCanvas()

    def initializeValues(self): 
        self.initializeCanvasSize()
        self.initializeCanvasSize()
        self.initializeFontSizeColor()
        self.initializeOffsets()
        self.tempCounter = 100
    
    def initializeCanvasSize(self):
        self.WINDOW_BUFFER = 2
        
        self.frame_rate = 80
        self.x0 = 0 + self.WINDOW_BUFFER
        self.x1 = 990
        self.y0 = 0 + self.WINDOW_BUFFER
        self.y1 = 80
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
        self.canvasWidth = 990
        self.canvasHeight = 425
        
        self.centerX = 495
        self.centerY = 275
        self.maxSpeed = 280
        
        self.circleX1 = 295
        self.circleX2 = 695
        self.circleY1 = 115
        self.circleY2 = 515
        
    def initializeFontSizeColor(self):
        self.backGroundColor = "white"
        self.backGroundFillColor = "white"
        self.outlineColor = "white"
        self.fillColor = "white"        
        self.textColor = "black"
        
        self.coolantLabelFont = "helvetica 30 bold"
        self.coolantTextFont = "helvetica 50 bold"
        
        self.chargeLabelFont = "helvetica 30 bold"
        self.chargeTextFont = "helvetica 50 bold"
        
        self.speedHubFont = "helvetica 100 bold"
        self.kphHubFont = "helvetica 10 bold"
        
        self.rpmHubTextFont = "helvetica 50 bold"
        self.rpmHubLabelFont = "helvetica 10 bold"
        
        self.motorTpsTextFont = "helvetica 50 bold"
        self.motorTpsLabelFont = "helvetica 30 bold"
        
        self.engineTpsTextFont = "helvetica 50 bold"
        self.engineTpsLabelFont = "helvetica 30 bold"
        
        
    def initializeOffsets(self):
        
        self.IMDLatchLabelOffsetX = 190
        self.IMDLatchLabelOffsetY = 20        

        self.TSMSLatchLabelOffsetX = 210
        self.TSMSLatchLabelOffsetY = 60
        
        self.cockpitBRBLatchLabelOffsetX = 700
        self.cockpitBRBLatchLabelOffsetY = 20
        
        self.BMSLatchLabelOffsetX = 790
        self.BMSLatchLabelOffsetY = 60
                      
    def makeMainFrame(self):
        self.styleName = "TFrame"
        self.style = ttk.Style()
        self.style.configure(self.styleName, background="white", outline="white")
        
        self.mainFrame = ttk.Frame(self.root, padding="0 0 0 0", style=self.styleName)
        self.mainFrame.grid(column=1, row=2, sticky=(N, E, W, S))
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        
    def createCanvas(self):
        self.canvas = Canvas(self.mainFrame, width=self.width + self.WINDOW_BUFFER, height=self.height, background=self.backGroundColor)
        self.canvas.grid(column=0, row=0, sticky=(N, E, W, S))
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill=self.backGroundFillColor)
        
        self.TSMSLatchLabel = self.canvas.create_text(self.x0 + self.TSMSLatchLabelOffsetX, self.y0 + self.TSMSLatchLabelOffsetY, text="TSMS LATCH ERROR", fill=self.textColor, font=self.chargeLabelFont)
        
        self.cockpitBRBLatchLabel = self.canvas.create_text(self.x0  + self.cockpitBRBLatchLabelOffsetX, self.y0 + self.cockpitBRBLatchLabelOffsetY, text="COCKPIT BRB LATCH ERROR", fill=self.textColor, font=self.coolantLabelFont)
        
        self.BMSLatchLabel = self.canvas.create_text(self.x0 + self.BMSLatchLabelOffsetX, self.y0 + self.BMSLatchLabelOffsetY, text="BMS LATCH ERROR", fill=self.textColor, font=self.engineTpsLabelFont)
        
        self.IMDLatchLabel = self.canvas.create_text(self.x0 + self.IMDLatchLabelOffsetX, self.y0 + self.IMDLatchLabelOffsetY, text="IMD LATCH ERROR", fill=self.textColor, font=self.motorTpsLabelFont)
        
    def updateIMDLatchWarning(self, pRPM=None):
        if pRPM is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.IMDLatchLabel, fill="white")
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.canvas.itemconfigure(self.IMDLatchLabel, fill="red")
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateIMDLatchWarning)
        
    def updateBMSLatchWarning(self, pUpdateBMSLatchWarning=None):
        if pUpdateBMSLatchWarning is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.BMSLatchLabel, fill="white")
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.charge = pCharge
            self.canvas.itemconfigure(self.BMSLatchLabel, fill="red")
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateBMSLatchWarning)
        
    def updateTSMSLatchWarning(self, pUpdateTSMSLatchWarning=None):
        if pUpdateTSMSLatchWarning is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.TSMSLatchLabel, fill="white")
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.engineTps = pEngineTPS
            self.canvas.itemconfigure(self.TSMSLatchLabel, fill="red")
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateTSMSLatchWarning)
        
    def updateCockPitBRBLatchWarning(self, pCockPitBRBLatchWarning=None):
        if pCockPitBRBLatchWarning is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                self.canvas.itemconfigure(self.cockpitBRBLatchLabel, fill="white")
                self.canvas.update()
            except ValueError:
                pass
        else:
            self.motorTps = pMotorTPS
            self.canvas.itemconfigure(self.cockpitBRBLatchLabel, fill="red")
            self.canvas.update()
        self.root.after(self.frame_rate, self.updateCockPitBRBLatchWarning)
        
if __name__ == "__main__":
    root = Tk()
    testRect = WarningRectangle(root)
     
    testRect.updateCockPitBRBLatchWarning()
    testRect.updateTSMSLatchWarning()
    testRect.updateBMSLatchWarning()
    testRect.updateIMDLatchWarning()
     
    root.mainloop()
