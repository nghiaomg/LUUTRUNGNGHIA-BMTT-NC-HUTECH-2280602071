def left_rotate(value, shift):
    return ((value << shift) | (value >> 32 (32 - shift))) & 0xFFFFFFFF
def md5(message):
    a = 0x7452301
    b = 0xEFCDA889
    c = 0x98BADCFE
    d = 0x10325476

    original_length = len(message)
