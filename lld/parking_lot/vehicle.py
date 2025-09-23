from abc import ABC
from vehicle_size import VehicleSize

class Vehicle:
    def __init__(self, license_plate: str, size: VehicleSize):
        self._license_plate = license_plate
        self._size = size
        
    def get_license_plate(self) -> str:
        return self._license_plate
    
    def get_size(self) -> VehicleSize:
        return self._size