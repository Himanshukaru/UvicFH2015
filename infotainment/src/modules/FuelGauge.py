from tkinter import *
from tkinter import ttk
import math
import time

class FuelGauge(object):
	def __init__(self, root):
		self.root = root

		self.initializeValues()
		self.makeMainFrame()
		self.makeCanvas()

	def initializeValues(self):
		self.fuel_gauge_image = PhotoImage(file='Resources/images/Increase_fuel_mileage-1.gif')
		self.current_kph = StringVar()
		self.current_kph.set(0)
		
		self.angle = StringVar()
		self.angle.set(0)
		
		self.radius = 125
		self.center = 160
		self.frame_rate = 150
		self.start_angle = 2.8476

		self.tempCounter = 0
		self.fuelLevel = 0

	def makeMainFrame(self):
		self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1)

	def makeCanvas(self):
		#Canvas to display Fuel gauge (320 x 180 image)
		self.fuel_gauge = Canvas(self.mainframe, width=320, height=180, background='#ffffff')
		self.fuel_gauge.create_image(self.center, 106, image=self.fuel_gauge_image)
		self.fuel_gauge.grid(column=0, row=0, sticky=(N,E,W,S))
		centerdot = self.fuel_gauge.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='red')
		self.line = self.fuel_gauge.create_line((self.center, self.center, self.center+self.radius*math.cos(self.start_angle), self.center-self.radius*math.sin(self.start_angle)), fill='red', width=5)
		
		#Canvas to display Fuel gauge warning light
		self.fuel_warning_light = Canvas(self.mainframe, width=35, height=50, background='#ff0000')
		self.fuel_warning_light.grid(column=1, row=0, sticky=(N,E,W,S))
		
		#Make a label that will display the current % Fuel
		self.current_kph_label = ttk.Label(self.mainframe, textvariable=self.current_kph, width=3, font="Helvetica 36 bold")
		self.current_kph_label.grid(column=0, row=1, sticky=(E))
		self.percent_fuel_text_label = ttk.Label(self.mainframe, text="% Fuel", font="Helvetica 10 bold")
		self.percent_fuel_text_label.grid(column=1, row=1, sticky=(W))

	def rotateLine(self):
		try:
			value = int(self.angle.get())
			if self.tempCounter <= 50 and self.tempCounter <= 100:
				self.tempCounter += 1
			elif self.tempCounter >= 0:
				self.tempCounter -= 1

			start_degree = self.start_angle*180/math.pi
			if (value > 100):
				value = 100
			if (value < 0):
				value = 0
			x = value

			self.current_kph.set(x)
			self.kph_rad = (self.start_angle-x*(math.pi/180)*1.44)
			if (x < 15):
				self.fuel_warning_light.configure(background ='#ff0000')
			elif ( x >= 15):
				self.fuel_warning_light.configure(background ='#00ff00')
			self.fuel_gauge.coords(self.line, (self.center, self.center, self.center+self.radius*math.cos(self.kph_rad), self.center-self.radius*math.sin(self.kph_rad)))
			self.fuel_gauge.update()
			self.fuel_warning_light.update()
		except ValueError:
			pass
		self.angle.set(self.tempCounter)
		self.root.after(self.frame_rate,self.rotateLine)