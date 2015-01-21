from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from tkinter import messagebox
import math
import time




#Does the math and rotates the dial to the requested %fuel position
#This is currently animated as a proof of concept
#Known issues:
#	input is not reasonably limited


class Display():
	def __init__(self):
		self.root = Tk()
		self.root.title("Fuel-Milage-test")
		self.root.attributes("-fullscreen",False)
		self.root.configure(background='#ffffff')
		self.root.bind()
		self.state = False
		self.root.bind("<F>", self.toggle_fullscreen)
		self.root.bind("<Escape>", self.end_fullscreen)
		
		self.fuel_guage_image = PhotoImage(file='Increase_fuel_mileage-1.gif')
		self.battery_guage_image = PhotoImage(file='Increase_bat_mileage-1.gif')
		self.speedo_image = PhotoImage(file='speedometer2.gif')
		self.start_angle=2.8476
		self.center = 160
		self.radius = 135
		self.frame_rate = 150

		
		self.current_kph = StringVar()
		self.current_kph.set(0)
		self.angle = StringVar()
		self.angle.set(0)
		
		self.current_charge = StringVar()
		self.current_charge.set(0)
		self.angle_charge = StringVar()
		self.angle_charge.set(0)
		
		self.current_speed = StringVar()
		self.current_speed.set(0)
		self.speed_angle = StringVar()
		self.speed_angle.set(0)
		self.start_angle2=4.33476
		self.center2 = 250
		self.radius2 = 250

		value =self.angle

		#Create the mainframe, configure it
		self.mainframe = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
		self.mainframe.columnconfigure(0, weight=1)
		self.mainframe.rowconfigure(0, weight=1)

		#Create the mainframe2, configure it
		self.mainframe2 = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe2.grid(column=0, row=1, sticky=(N, E, W, S))
		self.mainframe2.columnconfigure(0, weight=1)
		self.mainframe2.rowconfigure(0, weight=1)

		#Create the mainframe3, configure it		
		self.mainframe3 = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe3.grid(column=1, row=0, columnspan=1, rowspan=2, sticky=(N, E, W, S))
		self.mainframe3.columnconfigure(0, weight=1)
		self.mainframe3.rowconfigure(0, weight=1)

		#Create the mainframe4, configure it		
		self.mainframe4 = ttk.Frame(self.root, padding="0 0 0 0")
		self.mainframe4.grid(column=0, row=2, columnspan=2, rowspan=1, sticky=(N, E, W, S))
		self.mainframe4.columnconfigure(0, weight=1)
		self.mainframe4.rowconfigure(0, weight=1)

		#Canvas to display Fuel guage (320 x 180 image)
		self.fuel_guage = Canvas(self.mainframe, width=320, height=180, background='#ffffff')
		self.fuel_guage.create_image(self.center, 106, image=self.fuel_guage_image)
		self.fuel_guage.grid(column=0, row=0, sticky=(N,E,W,S))
		self.centerDot = self.fuel_guage.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='red')
		self.line1 = self.fuel_guage.create_line((self.center, self.center, self.center+self.radius*math.cos(self.start_angle), self.center-self.radius*math.sin(self.start_angle)), fill='red', width=5)
		#Canvas to display Fuel guage warning light
		self.fuel_warning_light = Canvas(self.mainframe, width=35, height=50, background='#ff0000')
		self.fuel_warning_light.grid(column=1, row=0, sticky=(N,E,W,S))
		#Make a label that will display the current % Fuel
		self.current_kph_label = ttk.Label(self.mainframe, textvariable=self.current_kph, width=3, font="Helvetica 36 bold")
		self.current_kph_label.grid(column=0, row=1, sticky=(E))
		self.percent_fuel_text_label = ttk.Label(self.mainframe, text="% Fuel", font="Helvetica 10 bold")
		self.percent_fuel_text_label.grid(column=1, row=1, sticky=(W))


		#Canvas to display Charge Guage (320 x 180 image)
		self.charge_guage = Canvas(self.mainframe2, width=320, height=180, background='#ffffff')
		self.charge_guage.create_image(self.center, 106, image=self.battery_guage_image)
		self.charge_guage.grid(column=0, row=0, sticky=(N,E,W,S))
		self.centerDot2 = self.charge_guage.create_oval(self.center-10, self.center-10, self.center+10, self.center+10, fill='red')
		self.line2 = self.charge_guage.create_line((self.center, self.center, self.center+self.radius*math.cos(self.start_angle), self.center-self.radius*math.sin(self.start_angle)), fill='red', width=5)
		#Canvas to display Fuel guage warning light
		self.charge_warning_light = Canvas(self.mainframe2, width=35, height=50, background='#ff0000')
		self.charge_warning_light.grid(column=1, row=0, sticky=(N,E,W,S))
		#Labels to display numeric value of battery condition
		self.current_charge_label = ttk.Label(self.mainframe2, textvariable=self.current_charge, width=3, font="Helvetica 36 bold")
		self.current_charge_label.grid(column=0, row=1, sticky=(E))
		self.percent_charge_text_label = ttk.Label(self.mainframe2, text="% SOC", font="Helvetica 10 bold")
		self.percent_charge_text_label.grid(column=1, row=1, sticky=(W))

		#Put in Speedometer.
		self.speedometer = Canvas(self.mainframe3, width=500, height=500, background='#ffffff')
		self.speedometer.create_image(self.center2, self.center2, image=self.speedo_image)
		self.speedometer.grid(column=0, row=1, sticky=(N,E,W,S))
		self.centerDot3 = self.speedometer.create_oval(self.center2-10, self.center2-10, self.center2+10, self.center2+10, fill='red')
		self.line3 = self.speedometer.create_line((self.center2, self.center2, self.center2+self.radius2*math.cos(self.start_angle2), self.center2-self.radius2*math.sin(self.start_angle2)), fill='red', width=5)

		self.info_label = ttk.Label(self.mainframe4, text="Formula Hybrid Vehicle GUI\nVERSION: CONCEPT DEMO\nMODE: DEMO", width=3, font="Helvetica 9 bold")
		self.info_label.grid(column=0, row=0, sticky=(N,E,W,S))


		self.rotateline()
		self.chargerotateline()
		self.rotateSpeedLine()
		self.testguage()
		self.root.mainloop()
		
	def toggle_fullscreen(self, event=None):
		self.state = not self.state  # Just toggling the boolean
		self.root.attributes("-fullscreen", self.state)
		return "break"
		
	def end_fullscreen(self, event=None):
		self.state = False
		self.root.attributes("-fullscreen", False)
		return "break"
		
	def rotateline(self):
		try:
			value = int(self.angle.get())
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
			self.fuel_guage.coords(self.line1, (self.center, self.center, self.center+self.radius*math.cos(self.kph_rad), self.center-self.radius*math.sin(self.kph_rad)))
			self.fuel_guage.update()
			self.fuel_warning_light.update()

		except ValueError:
			pass
		self.root.after(self.frame_rate,self.rotateline)	

	def chargerotateline(self):
		try:
			value = int(self.angle_charge.get())
			start_degree = self.start_angle*180/math.pi

			if (value > 100):
				value = 100
			if (value < 0):
				value = 0

			x = value
			self.current_charge.set(x)
			self.charge_rad = (self.start_angle-x*(math.pi/180)*1.44)
			if (x < 30):
				self.charge_warning_light.configure(background ='#ff0000')
				self.charge_warning_light.update()
			elif ( x >= 30):
				self.charge_warning_light.configure(background ='#00ff00')
				self.charge_warning_light.update()

			self.charge_guage.coords(self.line2, (self.center, self.center, self.center+self.radius*math.cos(self.charge_rad), self.center-self.radius*math.sin(self.charge_rad)))
			self.charge_guage.update()

		except ValueError:
			pass
		self.root.after(self.frame_rate,self.chargerotateline)


	def rotateSpeedLine(self):
		try:
			value = float(self.speed_angle.get())
			start_degree = self.start_angle2

			if (value > 260):
				value = 260
			if (value < 0):
				value = 0

			#self.current_speed.set(value)
			#self.current_speed = (self.start_angle-value*(math.pi/180)*1.44)
			self.the_speed=(start_degree-(value*(math.pi/180)*1.21818181))#*0.01745329)
			# print(self.the_speed)
			self.speedometer.coords(self.line3, (self.center2, self.center2, self.center2+self.radius2*math.cos(self.the_speed), self.center2-self.radius2*math.sin(self.the_speed)))
			self.speedometer.update()

		except ValueError:
			pass
		self.root.after(self.frame_rate,self.rotateSpeedLine)
	

	def testguage(self):
		fuelleft=int(self.angle.get())
		chargeleft=int(self.angle_charge.get())
		currentspeed=int(self.speed_angle.get())
		
		if(fuelleft<=0 and chargeleft<=0):
			self.angle.set(100)
			self.angle_charge.set(100)
			self.speed_angle.set(0)
		else:
			self.angle.set(fuelleft-1)
			self.angle_charge.set(chargeleft-2)
			self.speed_angle.set(currentspeed+1)

		self.root.after(self.frame_rate,self.testguage)


display = Display()