'''Write a Python program that converts a decimal number to its binary representation. The program should:

Take an integer input from the user.
Convert the decimal number to binary using the division-by-2 method.
Print the binary equivalent of the decimal number without using any built-in binary conversion methods.'''

import math
def BinToDec(decNum):
    pow=0
    binNum=0
    n=decNum
    while(decNum>0):
        rem=decNum%2
        binNum+=rem*int(math.pow(10,pow))
        pow+=1
        decNum=decNum//2
    print(f"Decimal to Binary Conversion of {n} : {binNum}")

n=int(input("Enter Decimal Number:"))
BinToDec(n)

    
