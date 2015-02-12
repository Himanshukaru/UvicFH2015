from tkinter import *
from tkinter import ttk
import math
import time

class Speedometer(object):
    root = Tk()
    def __init__(self):        
        self.initializeValues()
        self.makeMainFrame()
        self.makeCanvas()
        
        self.updateCharge()
        self.root.mainloop()


    def initializeValues(self):
        self.frame_rate = 80
        self.center = 110
        self.radius = 80
        self.pieAngle = 100
        
        self.piePositionAngle = 0
        self.tempCounter = 0 #TODO m: this will be the charge count; for now its a temp counter

    def makeMainFrame(self):
        self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
        self.mainframe.grid(column=1, row=0, columnspan=1, rowspan=2, sticky=(N, E, W, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

    def makeCanvas(self):
        self.chargePie = Canvas(self.mainframe, width=250, height=250, background='#ffffff')
        self.chargePie.grid(column=0, row=1, sticky=(N,E,W,S))
        self.chargePie.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline='green', start=self.piePositionAngle)
        
        self.chargeDeltaPie = self.chargePie.create_arc(self.center-self.radius, self.center-self.radius, self.center+self.radius, self.center+self.radius, style=PIESLICE, extent=self.pieAngle, outline='green', fill='green', start=self.piePositionAngle)

    def updateCharge(self):
        try:
            self.tempCounter += 1

            if (self.tempCounter > self.pieAngle):
                self.tempCounter = self.pieAngle
            if (self.tempCounter < self.piePositionAngle):
                self.tempCounter = self.piePositionAngle
                            
            self.chargePie.itemconfigure(self.chargeDeltaPie, extent=self.tempCounter)
            self.chargePie.update()
        except ValueError:
            pass
        self.root.after(self.frame_rate,self.updateCharge)
        
if __name__ == "__main__":
    
    testClass = Speedometer()