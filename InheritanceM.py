"""simple code of multiple inheritance"""

class car:
    @staticmethod
    def start():
        model = 1997
        print("Car started:")

class toyotacar(car):
    def __init__(self,brand):
        self.brand = brand
       
class fortuner(toyotacar):
    def __init__(self,type):
        self.type = type
     

car1 = fortuner("diesal")

car1.start()
print(car1.type)
