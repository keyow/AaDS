def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

print(next_power_of_2(3) )