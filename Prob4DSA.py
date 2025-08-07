'''Prob 4: Write a program using switch case which takes a value and prints the respective Size.
If size is 29 then its small
If size is 30 then its Medium
If size is 38 then its Large
If size is 42 then its XLarge
If size is not any of the above then Invalid.
Input: 29
Expected Output: 
Small'''
size = int(input("Enter the size: "))

if size == 29:
    print("Small")
elif size == 30:
    print("Medium")
elif size == 38:
    print("Large")
elif size == 42:
    print("XLarge")
else:
    print("Invalid")
