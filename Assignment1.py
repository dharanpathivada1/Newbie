m=int(input("enter the no of lines = "))
for i in range(m):
    print()
    for j in range(m-i):
        print(" ",end="")
    for k in range((2*i)+1):
        print("*",end="")
    for l in range(m-i):
        print("_",end="")
        