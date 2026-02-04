class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def welcome(self):
        x = self.name
        print("welcome new student:",x)

s1 = student("zayn",59)
s1.welcome()
print("The marks of new student is:",s1.marks)