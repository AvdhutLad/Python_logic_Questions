import math


n=int(input("Enter Number:"))
isPrime=True
if(n==2):
    print('2 is Prime Number')
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            isPrime=False
            break

    if isPrime:
        print(n,"is prime.")
    else:
        print(n,"is not prime.")