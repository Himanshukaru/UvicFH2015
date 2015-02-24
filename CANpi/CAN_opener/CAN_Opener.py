import struct
# Leaving these here, but they are not needed at this level for now
# ONE_BIT_MASK        = 0x1
# TWO_BIT_MASK        = 0X3
# THREE_BIT_MASK      = 0x7
# FOUR_BIT_MASK       = 0xF

# FIVE_BIT_MASK       = 0x1F
# SIX_BIT_MASK        = 0x3F
# SEVEN_BIT_MASK      = 0x7F
# EIGHT_BIT_MASK      = 0xFF

# NINE_BIT_MASK       = 0x1FF
# TEN_BIT_MASK        = 0x3FF
# ELEVEN_BIT_MASK     = 0x7FF
# TWELVE_BIT_MASK     = 0xFFF

# THRIRTEEN_BIT_MASK  = 0x1FFF
# FOURTEEN_BIT_MASK   = 0x3FFF
# FIFTEEN_BIT_MASK    = 0x7FFF
# SIXTEEN_BIT_MASK    = 0xFFFF

class Can_opener(object):
		"""
        How this works is to flatten the byte array, bit shift the flattened array, then mask it and return whatever falls out
        Works regardless of how or where the data is positioned in the array, but array topology must be known. I left pack_data
        and shift_mask as two functions since you really only need to flatten the data once per frame but you may need to shift
        mask it out multiple times.
        """
    def __init__(self):
        super(Can_opener, self).__init__()
        #self.arg = arg
    
    def pack_data(self, can_byte_array):
        buf=bytes()
        buf=buf.join((struct.pack('B', val) for val in can_byte_array))
        packed_can_data = int.from_bytes(buf, byteorder='big')
        return packed_can_data
    
    def shift_mask(self, start_loc, length, lumped_data, mask):
        shift = 64 - start_loc - length 
        lumped_data = lumped_data>>shift
        lumped_data = lumped_data & mask
        return lumped_data

#Just some testing
# test = Can_opener
# data = [0x31,0x36,0xB0,0xac,0x13,0x6B,0x0a,0x07]
# data_bytes = test.pack_data(data)
# print(test.shift_mask(8,16,data_bytes,SIXTEEN_BIT_MASK))
# print(test.shift_mask(36,16,data_bytes,SIXTEEN_BIT_MASK))