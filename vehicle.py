# pattern Builder
from abc import ABC, abstractmethod


class Vehicle:
    # def __init__(self, vehicle_type, max_speed, fuel_capacity, fuel_efficiency, extras=None):
    #     self.vehicle_type = vehicle_type
    #     self.max_speed = max_speed
    #     self.fuel_capacity = fuel_capacity
    #     self.fuel_efficiency = fuel_efficiency
    #     self.extras = extras or []
    #
    # def __str__(self):
    #     return (f"{self.vehicle_type}: Max Speed={self.max_speed}, Fuel Capacity={self.fuel_capacity}, "
    #             f"Fuel Efficiency={self.fuel_efficiency}, Extras={self.extras}")

    def __init__(self):
        self.features = []

    def add_feature(self, feature):
        self.features.append(feature)

    def __str__(self):
        return ', '.join(self.features)


class VehicleBuilder(ABC):
    def __init__(self):
        self.vehicle = None

    def create_new_vehicle(self):
        self.vehicle = Vehicle()

    @abstractmethod
    def set_vehicle_type(self):
        pass

    @abstractmethod
    def set_max_speed(self):
        pass

    @abstractmethod
    def set_fuel_capacity(self):
        pass

    @abstractmethod
    def set_fuel_efficiency(self):
        pass

    @abstractmethod
    def add_extra(self):
        pass

    def get_vehicle(self):
        return self.vehicle

    # def __init__(self):
    #     self.vehicle_type = None
    #     self.max_speed = None
    #     self.fuel_capacity = None
    #     self.fuel_efficiency = None
    #     self.extras = []
    #
    # def set_vehicle_type(self, vehicle_type):
    #     self.vehicle_type = vehicle_type
    #
    # def set_max_speed(self, max_speed):
    #     self.max_speed = max_speed
    #
    # def set_fuel_capacity(self, fuel_capacity):
    #     self.fuel_capacity = fuel_capacity
    #
    # def set_fuel_efficiency(self, fuel_efficiency):
    #     self.fuel_efficiency = fuel_efficiency
    #
    # def add_extra(self, extra):
    #     self.extras.append(extra)
    #
    # def build(self):
    #     return Vehicle(self.vehicle_type, self.max_speed, self.fuel_capacity, self.fuel_efficiency, self.extras)
