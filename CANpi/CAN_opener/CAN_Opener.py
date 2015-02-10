import struct
#All the mask we will need most likely, easy to add more, should be globals
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

class Can_opener(object):
	"""
	How this works is to flaten the byte array, bit shift the flattened array, then mask it and return whatever falls out
	Works regarless of how or where the data is positioned in the array, but array topology must be known. I left pack_data
	and shift_mask as two functions since you really only need to flaten the data once per frame but you may need to shift 
	mask it out multiple times. 
	"""
	def __init__(self, arg):
		super(Can_opener, self).__init__()
		self.arg = arg
	
	def pack_data(can_byte_array):
	    buf=bytes()
	    buf=buf.join((struct.pack('B', val) for val in can_byte_array))
	    packed_can_data = int.from_bytes(buf, byteorder='big')
	    return packed_can_data

	def shift_mask(start_loc, length, lumped_data, filter):
	    shift = 64 - start_loc - length
	    lumped_data = lumped_data>>shift
	    lumped_data = lumped_data & filter
	    return lumped_data



#Just some testin'
test = Can_opener
data = [0x31,0x36,0xB0,0xac,0x13,0x6B,0x0a,0x07]
data_bytes = Can_opener.pack_data(data)
print(Can_opener.shift_mask(8,16,data_bytes,SIXTEEN_BIT_MASK))
print(Can_opener.shift_mask(36,16,data_bytes,SIXTEEN_BIT_MASK))



