from tkinter import *
from tkinter import ttk
import math
import time

class ChargeGauge(object):
	def __init__(self, root):
		self.root = root

		self.initializeValues()
		self.makeMainFrame()
		self.makeCanvas()

	def initializeValues(self):
		self.battery_guage_image = PhotoImage(file='Resources/images/Increase_bat_mileage-1.gif')

		self.current_charge = StringVar()
		self.current_charge.set(0)
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
		self.mainframe.grid(column=0, row=1, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1)

	def makeCanvas(self):
		#Canvas to display Charge Guage (320 x 180 image)
		self.charge_guage = Canvas(self.mainframe, width=320, height=180, background='#ffffff')
		self.charge_guage.create_image(self.center, 106, image=self.battery_guage_image)
		self.charge_guage.grid(column=0, row=0, sticky=(N,E,W,S))
		self.charge_guage.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='red')
		self.line = self.charge_guage.create_line((self.center, self.center, self.center+self.radius*math.cos(self.start_angle), self.center-self.radius*math.sin(self.start_angle)), fill='red', width=5)
		#Canvas to display Fuel guage warning light
		self.charge_warning_light = Canvas(self.mainframe, width=35, height=50, background='#ff0000')
		self.charge_warning_light.grid(column=1, row=0, sticky=(N,E,W,S))
		#Labels to display numeric value of battery condition
		self.current_charge_label = ttk.Label(self.mainframe, textvariable=self.current_charge, width=3, font="Helvetica 36 bold")
		self.current_charge_label.grid(column=0, row=1, sticky=(E))
		self.percent_charge_text_label = ttk.Label(self.mainframe, text="% SOC", font="Helvetica 10 bold")
		self.percent_charge_text_label.grid(column=1, row=1, sticky=(W))

	def rotateLine(self):
		try:
			value = int(self.angle.get())
			start_degree = self.start_angle*180/math.pi

			if self.tempCounter <= 50 and self.tempCounter <= 100:
				self.tempCounter += 1
			elif self.tempCounter >= 0:
				self.tempCounter -= 1

			x = value

			self.current_charge.set(x)
			self.charge_rad = (self.start_angle-x*(math.pi/180)*1.44)

			if (x < 30):
				self.charge_warning_light.configure(background ='#ff0000')
				self.charge_warning_light.update()
			elif ( x >= 30):
				self.charge_warning_light.configure(background ='#00ff00')
				self.charge_warning_light.update()

			self.charge_guage.coords(self.line, (self.center, self.center, self.center+self.radius*math.cos(self.charge_rad), self.center-self.radius*math.sin(self.charge_rad)))
			self.charge_guage.update()
		except ValueError:
			pass
		self.angle.set(self.tempCounter)
		self.root.after(self.frame_rate,self.rotateLine)