"""
Pages: 34, 35
Image: 13, 14
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info_vehicle(self):
        print(f"Vehicle infos: '{self.brand}' and '{self.model}'")

class Navigation:
    def __init__(self, gps_local):
        self.gps_local = gps_local

    def info_navigation(self):
        print(f"Navigation infos: '{self.gps_local}'")

class Cargo:
    def __init__(self, capacity):
        self.capacity = capacity

    def info_cargo(self):
        print(f"Capacity cargo infos: {self.capacity} Kg")
    
# Class that inherits all others
class HybridVehicle(Vehicle, Navigation, Cargo):
    def __init__(self, brand, model, gps_local, capacity):
        Vehicle.__init__(self, brand, model)
        Navigation.__init__(self, gps_local)
        Cargo.__init__(self, capacity)

    def info_complete(self):
        self.info_vehicle()
        self.info_navigation()
        self.info_cargo()

hybrid_vehicle = HybridVehicle("Chevrolet", "S10", "Brazil", 650)
hybrid_vehicle.info_complete()
