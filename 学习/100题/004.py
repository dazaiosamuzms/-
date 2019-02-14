def count_of_1bits(value):
    n = 0
    while value:
        value &= value - 1
        n += 1
    return n

n = count_of_1bits(0b11001110)
print(n)