#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n=int(input("Enter line Count:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end='')
    for k in range(1,2*i):
        if k<=2*i-1:
            print("*",end='')
    print()

for i in range(n-1,0,-1):
    for j in range(1,n):
        if j<=n-i:
            print(" ",end='')
    for k in range(1,2*i):
        if k<=2*i:
            print("*",end='')
    print()
    
