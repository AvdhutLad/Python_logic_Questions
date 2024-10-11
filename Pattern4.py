#A
#BC
#DEF
#GHIJ
#KLMNO

line=int(input("Enter Lines:"))
ch=65
for i in range(1,line+1):
    for j in range(1,line+10):
        if j<=i:
            print(chr(ch),end='')
            ch=ch+1
    print()
