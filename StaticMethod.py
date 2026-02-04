""" Simple program for calculating Area and Vloume of a Room"""

class room:
    @staticmethod                   #using staticmethod
    def area(length,breadth):
        return length*breadth

    @staticmethod
    def volume(length,breadth,height):
        return length*breadth*height
    
r1 = room()
value = r1.area(4,5)
print("The area of room is:",value)

value = r1.volume(4,5,2)
print("Volume of the room is:",value)