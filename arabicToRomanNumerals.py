# -*- coding: utf-8 -*-

"""
Convert Arabic to Roman numerals.
This works for all numbers from 0 - 8999.

@author: Rob Tompkins
"""
#
# 20180115
#
# I was working on this at the end of last year.  I wanted to take this on as the first "challenging" problem since
# getting back into python.  I may learn ways down the road of making it more compact, but it may be less readable.
# It may already be unreadable enough.

# When counting in Roman numerals, exceptions occur at 4, 9, 40, 90, 400, 900, etc.  I called them subtract points.
# For numbers > 3999, the Romans used a bar over the numeral.  Here I have had to use a single quote.

romanSymbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M', "V'"]
romanValue = [1, 5, 10, 50, 100, 500, 1000, 5000]
subtractPoint = [4, 9, 40, 90, 400, 900, 4000]

def arabicToRomanNumerals(n):
    # Handling 4000 - 8999, MV' - V'MMMCMXCIX.
    rem = n % romanValue[7]
    if rem in range (subtractPoint[6], romanValue[7]):
        return romanSymbol[6] + romanSymbol[7] + handle_900_3999(n%romanValue[6])
    else:
        return romanSymbol[7] * (n//romanValue[7]) + handle_900_3999(rem)


def handle_900_3999(n):
    # Handle 900 - 3999, CM - MMMCMXCIX.
    rem = n % romanValue[6]
    if rem in range (subtractPoint[5], romanValue[6]):
        return romanSymbol[6] * (n//romanValue[6]) + romanSymbol[4] + romanSymbol[6] + handle_90_399(n%romanValue[4])
    else:
        return romanSymbol[6] * (n//romanValue[6]) + handle_400_899(rem)

def handle_400_899(n):
    # Handling 400 - 899, CD - DCCCXCIX.
    rem = n % romanValue[5]
    if rem in range (subtractPoint[4], romanValue[5]):
        return romanSymbol[4] + romanSymbol[5] + handle_90_399(n%romanValue[4])
    else:
        return romanSymbol[5] * (n//romanValue[5]) + handle_90_399(rem)

def handle_90_399(n):
    # Handle 90 - 399, XC - CCCXCIX
    rem = n % romanValue[4]
    if rem in range (subtractPoint[3], romanValue[4]):
        return romanSymbol[4] * (n//romanValue[4]) + romanSymbol[2] + romanSymbol[4] + handle_9_39(n%romanValue[2])
    else:
        return romanSymbol[4] * (n//romanValue[4]) + handle_40_89(rem)

def handle_40_89(n):
    # Handling 40 - 89, XL - LXXXIX.
    rem = n % romanValue[3]
    if rem in range (subtractPoint[2], romanValue[3]):
        return romanSymbol[2] + romanSymbol[3] + handle_9_39(n%romanValue[2])
    else:
        return romanSymbol[3] * (n//romanValue[3]) + handle_9_39(rem)

def handle_9_39(n):
    # Handle 9 - 39, IX - XXXIX.
    rem = n % romanValue[2]
    if rem in range (subtractPoint[1], romanValue[2]):
        return romanSymbol[2] * (n//romanValue[2]) + romanSymbol[0] + romanSymbol[2]
    else:
        return romanSymbol[2] * (n//romanValue[2]) + handle_4_8(rem)

def handle_4_8(n):
    #Handle 4 - 8, IV - VIII.
    rem = n % romanValue[1]
    if rem in range (subtractPoint[0], romanValue[1]):
        # Note: First expression below is just for attempted symmetry.
        return romanSymbol[1] * (n//romanValue[1]) + romanSymbol[0] + romanSymbol[1]
    else:
        return romanSymbol[1] * (n//romanValue[1]) + handle_1_3(rem)

def handle_1_3(n):
# Handle 1 - 3.
    return  romanSymbol[0] * n

print()
print('This program converts a range of numbers in Arabic numerals up to 8999 to Roman numerals. \n')
print('Enter beginning number: ', end='')
startNumber = int(input())
print('Enter ending number: ', end='')
endNumber = int(input())

for i in range (startNumber, endNumber+1):
    print('Arabic = ', i, '    Roman  = ', arabicToRomanNumerals(i))

