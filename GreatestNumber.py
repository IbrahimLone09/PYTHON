"""Finding greatest of three numbers 
    entered by the user"""
a=int(input("Enter first Number:"))
b=int(input("Enter second Number:"))
c=int(input("Enter third Number:"))
if(a > b and a > c):
    print("First number is greatest:",a)
elif(b > a and b > c):
    print("Second number is greatest:",b)
elif(a == b ==c ):
    print("Equal numbers",c)
else:
    print("Third number is greatest:",c)
