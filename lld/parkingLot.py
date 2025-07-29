import string

"""
Source: https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/parking-lot.md 
Requirements
- The parking lot should have multiple levels, each level with a certain number of parking spots.
- The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
- Each parking spot should be able to accommodate a specific type of vehicle.
- The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
- The system should track the availability of parking spots and provide real-time information to customers.
- The system should handle multiple entry and exit points and support concurrent access.
"""

class Vehicle:
    def __init__(self, type):
        self.type = type
        self.parking_spot = []
        
    def enter(self, parking_lot):
        parking_lot.occupySpot(self)
        
    def exit(self, parking_lot):
        parking_lot.emptySpot(self)
        
class ParkingLot:
    def __init__(self):
        self.parking_lot = []
        
    def add_level(self, spots):
        self.parking_lot.append(Level(spots))
    
    def occupySpot(self, automobile: Vehicle) -> str:
        for level in self.parking_lot:
            for idx in range(len(level.level)):
                if level.level[idx] == 0:
                    level.level[idx] = automobile.type
                    automobile.parking_spot = [self.parking_lot.index(level), idx]
                    print("Your parking spot is: ", automobile.parking_spot)
                    return

        
    def emptySpot(self, automobile: Vehicle) -> str:
        x, y = automobile.parking_spot
        self.parking_lot[x].level[y] = 0
        print("Thank you for coming!")
        
    def getInfo(self):
        for level in self.parking_lot:
            print(level.level)
    
class Level:
    def __init__(self, spots):
        self.spots = spots
        self.level = [0] * spots
        
class Spot:
    def __init__(self, type):
        self.type = type
        
def main():
    p1 = ParkingLot()
    p1.add_level(5)
    p1.add_level(3)
    p1.add_level(2)
    
    mom_car = Vehicle("car")
    mom_car.enter(p1)
    p1.getInfo()
    mom_car.exit(p1)
    p1.getInfo()
        
main()