from tkinter import *
from tkinter import ttk
import math
import time

class Speedometer(object):
	def __init__(self, root):
		self.root = root

		self.initializeValues()
		self.makeMainFrame()
		self.makeCanvas()

	def initializeValues(self):
		self.speedo_image = PhotoImage(file='Resources/images/speedometer2.gif')
		self.current_speed = StringVar()
		self.current_speed.set(0)

		self.angle = StringVar()
		self.angle.set(0)
		
		self.radius = 250
		self.center = 250
		self.frame_rate = 150
		self.start_angle = 4.33476

		self.tempCounter = 0
		self.fuelLevel = 0

	def makeMainFrame(self):
		self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe.grid(column=1, row=0, columnspan=1, rowspan=2, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1)

	def makeCanvas(self):
		self.speedometer = Canvas(self.mainframe, width=500, height=500, background='#ffffff')
		self.speedometer.create_image(self.center, self.center, image=self.speedo_image)
		self.speedometer.grid(column=0, row=1, sticky=(N,E,W,S))
		self.speedometer.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='red')
		self.line = self.speedometer.create_line((self.center, self.center, self.center+self.radius*math.cos(self.start_angle), self.center-self.radius*math.sin(self.start_angle)), fill='red', width=5)
		
		# Make the label to display the speed in numerical value
		self.current_speed_label = ttk.Label(self.mainframe, textvariable=self.current_speed, width=3, font="Helvetica 36 bold")
		self.current_speed_label.grid(column=0, row=1, sticky=(E))
		self.current_speed_text_label = ttk.Label(self.mainframe, text="KPH", font="Helvetica 10 bold")
		self.current_speed_text_label.grid(column=1, row=1, sticky=(W))

	def rotateLine(self):
		try:
			value = float(self.angle.get())
			start_degree = self.start_angle

			self.tempCounter += 1

			if (self.tempCounter > 260):
				self.tempCounter = 260
			if (self.tempCounter < 0):
				tempCounter = 0

			self.the_speed=(start_degree-(value*(math.pi/180)*1.21818181))#*0.01745329)
			self.current_speed.set(self.tempCounter)

			self.speedometer.coords(self.line, (self.center, self.center, self.center+self.radius*math.cos(self.the_speed), self.center-self.radius*math.sin(self.the_speed)))
			self.speedometer.update()
		except ValueError:
			pass
		self.angle.set(self.tempCounter)
		self.root.after(self.frame_rate,self.rotateLine)