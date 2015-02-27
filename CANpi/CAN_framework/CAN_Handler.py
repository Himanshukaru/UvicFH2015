from CAN_Opener import *
from CAN_Main import *

ONE_BIT_MASK        = 0x1
TWO_BIT_MASK        = 0X3
THREE_BIT_MASK      = 0x7
FOUR_BIT_MASK       = 0xF

FIVE_BIT_MASK       = 0x1F
SIX_BIT_MASK        = 0x3F
SEVEN_BIT_MASK      = 0x7F
EIGHT_BIT_MASK      = 0xFF

NINE_BIT_MASK       = 0x1FF
TEN_BIT_MASK        = 0x3FF
ELEVEN_BIT_MASK     = 0x7FF
TWELVE_BIT_MASK     = 0xFFF

THRIRTEEN_BIT_MASK  = 0x1FFF
FOURTEEN_BIT_MASK   = 0x3FFF
FIFTEEN_BIT_MASK    = 0x7FFF
SIXTEEN_BIT_MASK    = 0xFFFF

class CAN_Handler(CAN_Main):
	"""
	This class extends CAN_Main, and as such should be the one created by the main app

	This will be the module to extact data from our messages
	This is hardcoded, so if stuff changes this needs to changes
	
	prototypes for can_tools
	shift_mask(start_loc, length, lumped_data, mask):
	pack_data(can_byte_array):

	"""	
	def __init__(self, arg):
		super(CAN_Handler, self).__init__()
		can_tools = CAN_Opener()

	def message_select(pCAN_frame):
		switch(self.pCAN_frame.abitration_id){
			case(0x100):
				self.message_one(pCAN_frame.data)
			case(0x200):
				self.message_two(pCAN_frame.data)
			case(0x300):
				self.message_three(pCAN_frame.data)
			case(0x400):
				self.message_four(pCAN_frame.data)
			default:
				pass
		}

	def message_one(data): #Engine Signals
		msg_one_bits = self.can_tools.pack_data(data)
		self.set_engine_coolant_temp(data[0])
		self.set_engine_torque(data[1])
		self.set_engine_RPM(self.can_tools.shift_mask(16, 16, msg_one_bits, SIXTEEN_BIT_MASK))
		self.set_throttle_percent(data[4])

	def message_two(data): #Warnings
		msg_two_bits = self.can_tools.pack_data(data)
		self.set_warning_ess_overtemp(self.can_tools.shift_mask(0, 1, msg_two_bits, ONE_BIT_MASK))
		self.set_warning_fuel_level_low(self.can_tools.shift_mask(1, 1, msg_two_bits, ONE_BIT_MASK))
		self.set_warning_glv_cockpit_brb(self.can_tools.shift_mask(2, 1, msg_two_bits, ONE_BIT_MASK))
		self.set_warning_glv_soc_low(self.can_tools.shift_mask(3, 1, msg_two_bits, ONE_BIT_MASK))
		self.set_warning_motor_over_temp(self.can_tools.shift_mask(4, 1, msg_two_bits, ONE_BIT_MASK))
		self.set_warning_transmission_failure(self.can_tools.shift_mask(5, 1, msg_two_bits, ONE_BIT_MASK))
	
	def message_three(data): #Electrical Systems
		self.set_ess_soc(data[0])
		self.set_ess_voltage(data[1])

	def message_four(data): #Control 
		msg_four_bits = self.can_tools.pack_data(data)
		self.set_current_control_mode(self.can_tools.shift_mask(0, 2, msg_four_bits, TWO_BIT_MASK))
		self.set_current_gear(self.can_tools(2, 4, msg_four_bits, FOUR_BIT_MASK))
		self.set_vehicle_speed(data[2])
		self.set_engery_budget_status(data[3])

