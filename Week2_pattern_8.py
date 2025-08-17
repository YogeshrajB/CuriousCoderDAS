n = int(input("enter the num:"))
for i in range(1,n*2):
    if i>n:
        x= 2*n-i
    else:
        x=i
    for j in range(0,x):
        print("*",end="")
    print("")
    
