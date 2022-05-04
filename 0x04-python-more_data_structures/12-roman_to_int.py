#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if roman_string == "":
        return 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    int_val = 0
    for i in range(len(roman_string)):
        if i > 0 and dic[roman_string[i]] > dic[roman_string[i - 1]]:
            int_val += dic[roman_string[i]] - 2 * dic[roman_string[i - 1]]
        else:
            int_val += dic[roman_string[i]]
    return int_val
