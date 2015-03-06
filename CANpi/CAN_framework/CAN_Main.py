import can
import CAN_Handler

can.rc['interface'] = 'socketcan_native'
from can.interfaces.interface import Bus
can_interface = "can0"

class CAN_Main(object):
	"""
	The gem of our CAN collection
	
	There should be:
	Signals | Messages
	--------+---------
	16      | 4

	Each has a Previous & Current
	Each has a update boolean
	Each has a set_value Function
	All are init to 0/False unless otherwise specified

	PROTOTYPE:
		def __init__
			self.current_PARAM = 0 
			self.previous_PARAM = 0
			self.update_PARAM = False

		def set_PARAM(pValue):
			self.previous_PARAM = self.current_PARAM
			self.current_PARAM = pValue
			if(self.previous_PARAM != self.current_PARAM):
			self.update_PARAM = True

	ADD READ FROM CAN STUFF
		pollBus() in FHguiTest
		can message read
	"""
	def __init__(self):
		#super(CAN_Main, self).__init__()
		#self.can_handler = CAN_Handler.CAN_Handler()
		#self.bus = Bus(can_interface)

		#Engine Signals
		self.current_engine_coolant_temp = 0 
		self.previous_engine_coolant_temp = 0
		self.update_engine_coolant_temp = False
		
		self.current_engine_torque = 0
		self.previous_engine_torque = 0
		self.update_engine_torque = False
		
		self.current_engine_RPM = 0
		self.previous_engine_RPM = 0
		self.update_engine_RPM = False
		
		self.current_throttle_percent = 0
		self.previous_throttle_percent = 0
		self.update_throttle_percent = False

		#Warnings
		self.current_warning_ess_overtemp = 0
		self.previous_warning_ess_overtemp = 0
		self.update_warning_ess_overtemp = False

		self.current_warning_fuel_level_low = 0
		self.previous_warning_fuel_level_low = 0
		self.update_warning_fuel_level_low = False

		self.current_warning_glv_cockpit_brb = 0
		self.previous_warning_glv_cockpit_brb = 0
		self.update_warning_glv_cockpit_brb = False

		self.current_warning_glv_soc_low = 0
		self.previous_warning_glv_soc_low = 0
		self.update_warning_glv_soc_low = False

		self.current_warning_motor_over_temp = 0
		self.previous_warning_motor_over_temp = 0
		self.update_warning_motor_over_temp = False

		self.current_warning_transmission_failure = 0 
		self.previous_warning_transmission_failure = 0
		self.update_warning_transmission_failure = False
	
		#self.#Electrical Systems
		self.current_ess_soc = 0
		self.previous_ess_soc = 0
		self.update_ess_soc = False

		self.current_ess_voltage = 0
		self.previous_ess_voltage = 0
		self.update_ess_voltage = False

		#self.#Control 
		self.current_current_control_mode = 0 #not confusing at all
		self.previous_current_control_mode = 0
		self.update_current_control_mode = False

		self.current_current_gear = 0
		self.previous_current_gear = 0
		self.update_current_gear = False

		self.current_vehicle_speed = 0
		self.previous_vehicle_speed = 0
		self.update_vehicle_speed = False

		self.current_engery_budget_status = 0
		self.previous_engery_budget_status = 0
		self.update_engery_budget_status = False

	def pollBus(self):
		try:	
			msg = self.bus.recv()
			self.process_CAN_message(msg)
		except :
			print("TODO m: We need to catch this, yo")
			raise

	def process_CAN_message(self, pCan_frame):
		self.can_handler.message_select(pCan_frame)

	#engine coolant temp
	def set_engine_coolant_temp(self, pValue):
		self.previous_engine_coolant_temp = self.current_engine_coolant_temp
		self.current_engine_coolant_temp = pValue
		if(self.previous_engine_coolant_temp != self.current_engine_coolant_temp):
			self.update_engine_coolant_temp = True
			print("Engine Coolant temp update")
			print("here is the new val: " + str(pValue))

	#engine torque
	def set_engine_torque(self, pValue):
		self.previous_engine_torque = self.current_engine_torque
		self.current_engine_torque = pValue
		if(self.previous_engine_torque != self.current_engine_torque):
			self.update_engine_torque = True

	#engine RPM
	def set_engine_RPM(self, pValue):
		self.previous_engine_RPM = self.current_engine_RPM
		self.current_engine_RPM = pValue
		if(self.previous_engine_RPM == self.current_engine_RPM):
			self.update_engine_RPM = True

	#throttle percent
	def set_throttle_percent(self, pValue):
		self.previous_throttle_percent = self.current_throttle_percent
		self.current_throttle_percent = pValue
		if(self.previous_throttle_percent != self.current_throttle_percent):
			self.update_throttle_percent = True
	
	#warning ess over temp
	def set_warning_ess_overtemp(self, pValue):
		self.previous_warning_ess_overtemp = self.current_warning_ess_overtemp
		self.current_warning_ess_overtemp = pValue
		if(self.previous_warning_ess_overtemp != self.current_warning_ess_overtemp):
			self.update_warning_ess_overtemp = True

	#warning fuel level low
	def set_warning_fuel_level_low(self, pValue):
		self.previous_warning_fuel_level_low = self.current_warning_fuel_level_low
		self.current_warning_fuel_level_low = pValue
		if(self.previous_warning_fuel_level_low != self.current_warning_fuel_level_low):
			self.update_warning_fuel_level_low = True

	#warning glv cockpit brb
	def set_warning_glv_cockpit_brb(self, pValue):
		self.previous_warning_glv_cockpit_brb = self.current_warning_glv_cockpit_brb
		self.current_warning_glv_cockpit_brb = pValue
		if(self.previous_warning_glv_cockpit_brb != self.current_warning_glv_cockpit_brb):
			self.update_warning_glv_cockpit_brb = True

	#warning glv soc low
	def set_warning_glv_soc_low(self, pValue):
		self.previous_warning_glv_soc_low = self.current_warning_glv_soc_low
		self.current_warning_glv_soc_low = pValue
		if(self.previous_warning_glv_soc_low != self.current_warning_glv_soc_low):
			self.update_warning_glv_soc_low = True

	#warning motor over temp
	def set_warning_motor_over_temp(self, pValue):
		self.previous_warning_motor_over_temp = self.current_warning_motor_over_temp
		self.current_warning_motor_over_temp = pValue
		if(self.previous_warning_motor_over_temp != self.current_warning_motor_over_temp):
			self.update_warning_motor_over_temp = True

	#warning transmission failure
	def set_warning_transmission_failure(self, pValue):
		self.previous_warning_transmission_failure = self.current_warning_transmission_failure
		self.current_warning_transmission_failure = pValue
		if(self.previous_warning_transmission_failure != self.current_warning_transmission_failure):
			self.update_warning_transmission_failure = True

	#current ess soc
	def set_ess_soc(self, pValue):
		self.previous_ess_soc = self.current_ess_soc
		self.current_ess_soc = pValue
		if(self.previous_ess_soc != self.current_ess_soc):
			self.update_ess_soc = True

	#current ess voltage
	def set_ess_voltage(self, pValue):
		self.previous_ess_voltage = self.current_ess_voltage
		self.current_ess_voltage = pValue
		if(self.previous_ess_voltage != self.current_ess_voltage):
			self.update_ess_voltage = True

	#current control mode
	def set_current_control_mode(self, pValue):
		self.previous_current_control_mode = self.current_current_control_mode
		self.current_current_control_mode = pValue
		if(self.previous_current_control_mode != self.current_current_control_mode):
			self.update_current_control_mode = True

	#current gear
	def set_current_gear(self, pValue):
		self.previous_current_gear = self.current_current_gear
		self.current_current_gear = pValue
		if(self.previous_current_gear != self.current_current_gear):
			self.update_current_gear = True

	#vehicle speed
	def set_vehicle_speed(self, pValue):
		self.previous_vehicle_speed = self.current_vehicle_speed
		self.current_vehicle_speed = pValue
		if(self.previous_vehicle_speed != self.current_vehicle_speed):
			self.update_vehicle_speed = True

	#energy budget status
	def set_engery_budget_status(self, pValue):
		self.previous_engery_budget_status = self.current_engery_budget_status
		self.current_engery_budget_status = pValue
		if(self.previous_engery_budget_status != self.current_engery_budget_status):
			self.update_engery_budget_status = True

	def initializeInstances(self):
		self.can_handler = CAN_Handler.CAN_Handler()
		self.bus = Bus(can_interface)

if __name__ == "__main__":
	canTestMain = CAN_Main()
	canTestMain.initializeInstances()
	while True:
		canTestMain.pollBus()
