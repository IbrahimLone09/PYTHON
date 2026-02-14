""" using CLASS METHOD to change class attribute"""

class person:
    name = "ibrahim"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("Rahul")
print(p1.name)           #Rahul
print(person.name)       #Rahul