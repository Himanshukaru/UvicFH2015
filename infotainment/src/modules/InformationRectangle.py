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
        self.motorTps = 0
        self.engineTps = 0
        
    def initializeCanvasSize(self):
        self.WINDOW_BUFFER = 2
        
        self.frame_rate = 40
        self.x0 = 0 + self.WINDOW_BUFFER
        self.x1 = 990
        self.y0 = 0 + self.WINDOW_BUFFER
        self.y1 = 80
        
        self.width = self.x1 - self.x0
        self.height = self.y1 - self.y0
        
        self.canvasWidth = 970
        self.canvasHeight = 425
        
        self.centerX = 495
        self.centerY = 325
        self.maxSpeed = 280
        
        self.circleX1 = 295
        self.circleX2 = 695
        self.circleY1 = 165
        self.circleY2 = 565
        
    def initializeFontSizeColor(self):
        self.backGroundColor = "white"
        self.backGroundFillColor = "grey"
        self.outlineColor = "white"
        self.fillColor = "white"        
        self.textColor = "black"
        
        self.coolantLabelFont = "helvetica 30 bold"
        self.coolantTextFont = "helvetica 50 bold"
        
        self.chargeLabelFont = "helvetica 30 bold"
        self.chargeTextFont = "helvetica 50 bold"
        
        self.speedHubFont = "helvetica 100 bold"
        self.kphHubFont = "helvetica 30 bold"
        
        self.rpmHubTextFont = "helvetica 50 bold"
        self.rpmHubLabelFont = "helvetica 30 bold"
        
        self.motorTpsTextFont = "helvetica 50 bold"
        self.motorTpsLabelFont = "helvetica 30 bold"
        
        self.engineTpsTextFont = "helvetica 50 bold"
        self.engineTpsLabelFont = "helvetica 30 bold"
        
        
    def initializeOffsets(self):
        
        self.speedLabelOffsetX = 60
        self.speedLabelOffsetY = 10
        self.speedOffsetX = 60
        self.speedOffsetY = 10
        
        self.rpmLabelOffsetX = 100
        self.rpmLabelOffsetY = 50
        self.rpmOffsetX = 85
        self.rpmOffsetY = 50

        self.fuelLabelOffsetX = 200
        self.fuelLabelOffsetY = 50
        self.fuelOffsetX = 280
        self.fuelOffsetY = 50
        
        self.chargeLabelOffsetX = 160
        self.chargeLabelOffsetY = 30        
        self.chargeOffsetX = 380
        self.chargeOffsetY = 30

        self.coolantLabelOffsetX = 170
        self.coolantLabelOffsetY = 80
        self.coolantTempOffsetX = 380
        self.coolantTempOffsetY = 80
        
        self.engineTpsTextOffsetX = 940
        self.engineTpsTextOffsetY = 30
        self.engineTpsLabelOffsetX = 750
        self.engineTpsLabelOffsetY = 30
        
        self.motorTpsTextOffsetX = 940
        self.motorTpsTextOffsetY = 80
        self.motorTpsLabelOffsetX = 740
        self.motorTpsLabelOffsetY = 80
                      
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
        
        self.canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.outlineColor, fill="white")
        
        self.chargeText = self.canvas.create_text(self.x0 + self.chargeOffsetX, self.y0 + self.chargeOffsetY, text=self.charge, fill=self.textColor, font=self.chargeTextFont)
        self.chargeLabel = self.canvas.create_text(self.x0 + self.chargeLabelOffsetX, self.y0 + self.chargeLabelOffsetY, text="Battery SOC (%):", fill=self.textColor, font=self.chargeLabelFont)
        
        self.coolantText = self.canvas.create_text(self.x0 + self.coolantTempOffsetX, self.y0 + self.coolantTempOffsetY, text=self.coolant, fill=self.textColor, font=self.coolantTextFont)
        self.coolantLabel = self.canvas.create_text(self.x0 + self.coolantLabelOffsetX, self.y0 + self.coolantLabelOffsetY, text="Coolant Temp (F):", fill=self.textColor, font=self.coolantLabelFont)
        
        self.engineTpsText = self.canvas.create_text(self.x0 + self.engineTpsTextOffsetX, self.y0 + self.engineTpsTextOffsetY, text=self.engineTps, fill=self.textColor, font=self.engineTpsTextFont)
        self.engineTpsLabel = self.canvas.create_text(self.x0 + self.engineTpsLabelOffsetX, self.y0 + self.engineTpsLabelOffsetY, text="Engine TPS (%):", fill=self.textColor, font=self.engineTpsLabelFont)
        
        self.motorTpsText = self.canvas.create_text(self.x0 + self.motorTpsTextOffsetX, self.y0 + self.motorTpsTextOffsetY, text=self.motorTps, fill=self.textColor, font=self.motorTpsTextFont)
        self.motorTpsLabel = self.canvas.create_text(self.x0 + self.motorTpsLabelOffsetX, self.y0 + self.motorTpsLabelOffsetY, text="Motor TPS (%):", fill=self.textColor, font=self.motorTpsLabelFont)
        
        self.hubCircle = self.canvas.create_oval(self.circleX1, self.circleY1, self.circleX2, self.circleY2, outline=self.outlineColor, fill=self.backGroundFillColor)
        self.speedText = self.canvas.create_text(self.centerX + 80, self.centerY, text=self.speed, fill=self.textColor, font=self.speedHubFont, anchor="e")
        self.kphLabel = self.canvas.create_text(self.centerX + 140, self.centerY + 30, text="kph", fill=self.textColor, font=self.kphHubFont)
        
        self.rpmText = self.canvas.create_text(self.centerX + 80, self.centerY + 100, text=self.rpm, fill=self.textColor, font=self.rpmHubTextFont, anchor="e")
        self.rpmLabel = self.canvas.create_text(self.centerX + 140, self.centerY + 110, text="rpm", fill=self.textColor, font=self.rpmHubLabelFont)
        
    def updateCoolantRectangle(self, pCoolant):
        if pCoolant is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.coolantText, text=str(self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.coolantText, text=str(pCoolant))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateCoolantRectangle)
        
    def updateSpeedRectangle(self, pSpeed):
        if pSpeed is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.speedText, text=str(self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.speedText, text=str(pSpeed))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateSpeedRectangle)

    def updateRPMRectangle(self, pRPM):
        if pRPM is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.rpmText, text=str(self.tempCounter * 1000))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.rpmText, text=str(pRPM))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateRPMRectangle)
        
    def updateChargeRectangle(self, pCharge):
        if pCharge is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.chargeText, text=str(self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.chargeText, text=str(pCharge))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateChargeRectangle)
        
    def updateEngineTPS(self, pEngineTPS):
        if pEngineTPS is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.engineTpsText, text=str(self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.engineTpsText, text=str(pEngineTPS))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateEngineTPS)
        
    def updateMotorTPS(self, pMotorTPS):
        if pMotorTPS is None:
            try:
                self.tempCounter -= 1
    
                if (self.tempCounter >= self.y1):
                    self.tempCounter = self.y1
                if (self.tempCounter <= self.y0):
                    self.tempCounter = self.y0
                
                #self.canvas.itemconfigure(self.motorTpsText, text=str(self.tempCounter))
                #self.canvas.update()
            except ValueError:
                pass
        try:
            self.canvas.itemconfigure(self.motorTpsText, text=str(pMotorTPS))
            self.canvas.update()
        except:
            pass
        #self.root.after(self.frame_rate, self.updateMotorTPS)
