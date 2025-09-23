import threading
from typing import Dict, List, Optional
from parking_floor import ParkingFloor

# The **ParkingLot** class follows the Singleton pattern to ensure only one instance of the parking lot exists. 
# It maintains a list of levels and provides methods to park and unpark vehicles.

class ParkingLot:
    _instance = None
    _lock = threading.Lock()
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This is a singleton class!")
        self.levels: List[ParkingFloor] = []
        
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def add_level(self, floor: ParkingFloor) -> None:
        self.levels.append(floor)
    