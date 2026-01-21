"""Program to check if a Number is 
   multiple of other Number """
x=int(input("Enter number you want to check:"))
a=int(input("Enter number you want to check with:"))
if(x % a == 0):
    print("Multiple of Number:",a)
else:
    print("Not a multple:")