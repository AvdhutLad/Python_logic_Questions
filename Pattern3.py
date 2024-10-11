# 1
# 12
# 123
# 1234
# 12345

line=int(input("Enter Line:"))
for i in range(1,line+1):
    for j in range(1,line+1):
        if j<=i:
            print(j,end='')
        else:
            print('',end='')
    print()