# *****
# *   *
# *   *
# *****

def hollow_Rectangle(row, col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            if(i==1 or i==row or j==1 or j==col):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

row=int(input("Enter Row Count:"))
col=int(input("Enter Coulmun Count:"))
hollow_Rectangle(row, col)