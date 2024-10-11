# *****
# ****
# ***
# **
# *

line=int(input('Enter Number:'))
for i in range(1,line+1):
    for j in range(1,line+1):
        if j<=line-i+1:
            print("*",end='')
        else:
            print("",end='')
    print()