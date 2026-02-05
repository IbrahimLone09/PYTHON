"""simple code of single inheritance"""

class car:
    color = "black"

    @staticmethod
    def start():
        print("Car started:")

    @staticmethod
    def stop():
        print("Car stopped:")

class toyotacar(car):
    def __init__(self,name):
        self.name = name


car1 = toyotacar("Fortuner")
car2 = toyotacar("prius")
print(car1.start())
print(car1.name)

