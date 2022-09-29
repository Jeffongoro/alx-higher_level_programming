#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None) or (not isinstance(roman_string, str)):
        return 0

    number = []
    for i in roman_string:
        if i == "I":
            number.append(1)
        elif i == "V":
            number.append(5)
        elif i == "X":
            number.append(10)
        elif i == "L":
            number.append(50)
        elif i == "C":
            number.append(100)
        elif i == "D":
            number.append(500)
        elif i == "M":
            number.append(1000)

    total = 0
    while number:
        if len(number) == 1:
            total += number[0]
            break
        if (number[0] >= number[1]):
            total += number[0]
            number = number[1:]
        else:
            total += number[1] - number[0]
            number = number[2:]

    return total
