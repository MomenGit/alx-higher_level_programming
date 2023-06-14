#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    subtractive_forms = {'IV': 4, 'IX': 9,
                         'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    if roman_string in subtractive_forms:
        return subtractive_forms[roman_string]

    number = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        number = number + romans[i]

    return number
