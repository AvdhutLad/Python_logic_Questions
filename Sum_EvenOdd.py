# Question : Write a program that reads a set of integers, and then prints the sum of the 
# even and odd integers
n=input("Enter Number ',' Seprated List:").split(',')
even_sum=0
odd_sum=0
for i in n:
    if int(i)%2==0:
        even_sum=even_sum+int(i)
    else:
        odd_sum=odd_sum+int(i)

print("Even Number Sum:",even_sum)
print ("Odd Number Sum:",odd_sum)