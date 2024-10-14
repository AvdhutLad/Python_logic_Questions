'''Write a Python program that converts a binary number (entered as an integer) to its decimal equivalent. The program should:

Prompt the user to input a binary number.
Use a loop to process each digit of the binary number, multiplying each digit (either 0 or 1) by powers of 2 based on its position.
Sum the results to get the decimal equivalent.
Print the decimal equivalent of the input binary number.'''

import math
def BinToDec(binNum):
    pow=0
    decNum=0
    n=binNum
    while(binNum>0):
        lastDigit=binNum%10
        decNum+=lastDigit*int(math.pow(2,pow))
        pow+=1
        binNum=binNum//10
    print(f"Binary to Decimal Conversion of {n} : {decNum}")

n=int(input("Enter Binary Number:"))
BinToDec(n)

    
