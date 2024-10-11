"""Question:
Write a Python program to calculate the binomial coefficient, which represents the number of ways to choose k elements from a set of n elements. 
The binomial coefficient is given by the formula:
 
Implement a function binomial_coefficient(n, k) that takes two integers n and k as input and returns the binomial coefficient.

Sample Input:
mathematica
Copy code
Enter value of n: 5
Enter value of k: 2
Sample Output:
The binomial coefficient C(5, 2) is: 10
Constraints:
Assume n ≥ k ≥ 0.
Factorial grows very fast, so handle the calculations carefully to avoid overflow for large n.
This question is focused on using combinatorics to calculate the number of combinations possible for a given set of n elements. 

Logic:
The binomial factor is computed as n! / (k! * (n - k)!), where ! denotes the factorial of a number.
"""


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def BinomialFactor():
    n=int(input("Enter value of n:"))
    r=int(input("Enter Value of r:"))
    fact_n=factorial(n)
    fact_r=factorial(r)
    fact_r_n=factorial(n-r)
    result=int(fact_n/(fact_r*fact_r_n))
    print(f"Binomial fcator of {n}n{r} is {result}.")

BinomialFactor()