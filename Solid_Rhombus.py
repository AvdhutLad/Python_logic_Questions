#     *****
#    *****
#   *****
#  *****
# *****

n=int(input("Enter Line count:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end="")
    for j in range(1,n+1):
        print("*",end="")
    print()