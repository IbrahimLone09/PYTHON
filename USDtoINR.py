# PROGRAM TO CONVERT USD TO INR AND VICE VERSA 

print("WELCOME...")

print("Choose your currency:")
print("1. INR to USD")
print("2. USD to INR")

choice = int(input("Enter choice:"))

rate = 83

if choice == 1:
    inr = int(input("Enter  INR:"))
    print("USD = ",inr/rate)

elif choice == 2:
    usd = int(input("Enter USD:"))
    print("INR = ",usd*rate)

else:
    print("Invalid output:")