# 12345
# 1234
# 123
# 12
# 1

n=int(input("Enter line Count:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i+1:
            print(j,end="")
        else:
            print("",end="")
    print()