# *    
# **   
# ***
# ****
# *****
line=int(input("Enter Line Number:"))
for i in range(1,line+1):
    for j in range(1,line+1):
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()