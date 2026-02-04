""" Program to create a student class 
that takes name and marks of 
three students as arguments then 
creating a method to calculate average
"""

class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for value in self.marks:  # using for loop here
            sum += value
        print("Hi",self.name,"your average score is:", sum/3)

s1 = student("Hulk",([94,95,98]))
s1.get_avg()