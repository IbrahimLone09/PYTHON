start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

for num in range(start_num,end_num + 1):
    if num > 1:
        for i in range(2,int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
            
   