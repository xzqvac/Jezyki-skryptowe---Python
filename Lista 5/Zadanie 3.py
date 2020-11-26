def rom2dec(value):
    dec = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    previous_number = 0
    for i in value[::-1]:
        if dec[i] >= previous_number:
            result += dec[i]
        else:
            result -= dec[i]
        previous_number = dec[i]
    return result


print(rom2dec("XX"))

