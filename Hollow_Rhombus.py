#     *****
#    *   *
#   *   *
#  *   *
# *****

n=int(input("Enter line Count:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end='')

    for k in range(1,n+1):
        if(k==1 or k==n or i==1 or i==n):
            print("*",end='')
        else:
            print(" ",end='')
    print()
