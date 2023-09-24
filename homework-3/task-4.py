def validate_unicode(arr):
    """
    Modes:
    0 - undefined
    1 - 1 byte
    2 - 2 bytes
    3 - 3 bytes
    4 - 4 bytes
    :param arr: codes array
    :return: True if unicode sequence is valid, otherwise False.
    """
    mode = 0
    counter = 0  # counter of '10xxxxxx' bytes
    for code in arr:
        if code & 128 == 0 or code & 224 == 192 or code & 240 == 224 or code & 248 == 240:
            if mode != 0 and counter < mode - 1:
                return False
            counter = 0
            if code & 80 == 0:
                mode = 1
            elif code & 224 == 192:
                mode = 2
            elif code & 240 == 224:
                mode = 3
            elif code & 248 == 240:
                mode = 4
        elif code & 192 == 128:
            if mode == 0:
                return False
            counter += 1
            if counter > mode - 1:
                return False
        else:
            return False
    if counter != mode - 1:
        return False
    return True


# Valid
example = [
    int("11000101", 2),  # 2 byte mode
    int("10000010", 2),  # byte 2
    int("00000001", 2)   # 1 byte mode
]

print(validate_unicode(example))

# Invalid
example = [
    int("10110011", 2),  # << Starts with 10 without mode byte
    int("10000010", 2),
    int("00000001", 2)
]
print(validate_unicode(example))

# Valid
example = [
    int("11110000", 2),  # 4 byte mode
    int("10000010", 2),  # byte 2
    int("10000001", 2),  # byte 3
    int("10010001", 2)   # byte 4
]
print(validate_unicode(example))

# Invalid
example = [
    int("11110000", 2),  # 4 byte mode
    int("10000010", 2),  # byte 2
    int("10000001", 2),  # byte 3
    #  Need one more here
]
print(validate_unicode(example))

# Invalid
example = [
    int("01110110", 2),  # 1 byte mode
    int("00010110", 2),  # 1 byte mode
    int("01111010", 2),  # 1 byte mode
    int("11011010", 2),  # 2 bytes mode
    int("10111010", 2),  # byte 2
    int("10111010", 2)   # << Redundant
]
print(validate_unicode(example))

# Valid
example = [
    int("11100110", 2),  # 3 byte mode
    int("10110111", 2),  # byte 2
    int("10000101", 2),  # byte 3
    int("00000101", 2),  # 1 byte mode
    int("11100110", 2),  # 3 byte mode
    int("10110111", 2),  # byte 2
    int("10000101", 2),  # byte 3
    int("11110000", 2),  # 4 byte mode
    int("10000010", 2),  # byte 2
    int("10000001", 2),  # byte 3
    int("10010001", 2),   # byte 4
    int("11000101", 2),  # 2 byte mode
    int("10000010", 2),  # byte 2
    int("00000001", 2)   # 1 byte mode
]
print(validate_unicode(example))
