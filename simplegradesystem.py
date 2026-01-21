#simple grade system based on marks
marks=int(input("Enter the marks of a student:"))
if(marks>= 90):
    marks="Grade A"
elif(marks>= 80 and marks < 90):
    marks="Grade B"
elif(marks>= 70 and marks< 80):
    marks="Grade C"
else:
    marks="Grade D"
print("The Grade of a student is:",marks)
