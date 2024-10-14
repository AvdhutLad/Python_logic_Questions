'''Write a Java program that finds and prints all prime numbers in a given range starting from 2 up to a user-defined number. The program should:

Define a method isPrime(int n) that checks whether a number n is prime. This method should return true if n is prime and false otherwise.
Define another method primeInRange(int number) that prints all prime numbers between 2 and the input number.
In the main() method, prompt the user to input an integer representing the upper bound of the range.
The program should print all prime numbers from 2 up to the input number.'''

import math
def isPrime(n):
    for i in range (2,int(math.sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def Primerange(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=" ")


number=int(input("Enter Number:"))
print(f"Prime numbers in range 1 to {number}:")
Primerange(number)