# pattern Builder
from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, vehicle_type, max_speed, fuel_capacity, fuel_efficiency, extras=None):
        # self.features = []
        self.vehicle_type = vehicle_type
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity
        self.fuel_efficiency = fuel_efficiency
        self.extras = extras or []

    def __str__(self):
        return (f"{self.vehicle_type}: Max Speed={self.max_speed}, Fuel Capacity={self.fuel_capacity}, "
                f"Fuel Efficiency={self.fuel_efficiency}, Extras={self.extras}")

    # def add_feature(self, feature):
    #     self.features.append(feature)

    # def __str__(self):
    #     return ', '.join(self.features)


class VehicleBuilder(ABC):
    def __init__(self):
        self.vehicle_type = None
        self.max_speed = None
        self.fuel_capacity = None
        self.fuel_efficiency = None
        self.extras = []

    def create_new_vehicle(self):
        return Vehicle(self.vehicle_type,
                       self.max_speed,
                       self.fuel_capacity,
                       self.fuel_efficiency,
                       self.extras)

    @abstractmethod
    def set_vehicle_type(self):
        pass

    def set_max_speed(self, speed):
        self.max_speed = speed

    def set_fuel_capacity(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def set_fuel_efficiency(self, fuel_efficiency):
        self.fuel_efficiency = fuel_efficiency

    def add_extra(self, extra: list):
        self.extras.extend(extra)


class CarBuilder(VehicleBuilder):
    def set_vehicle_type(self):
        self.vehicle_type = 'Type: Car'


class MotorcycleBuilder(VehicleBuilder):
    def set_vehicle_type(self):
        self.vehicle_type = 'Type: Motorcycle'


class TruckBuilder(VehicleBuilder):
    def set_vehicle_type(self):
        self.vehicle_type = 'Type: Truck'


class Director:
    def __init__(self, builder: VehicleBuilder):
        self._builder = builder
        # self.vehicle = None

    def construct_vehicle(self, max_speed, fuel_capacity, fuel_efficiency, extra):
        self._builder.set_vehicle_type()
        self._builder.set_max_speed(max_speed)
        self._builder.set_fuel_capacity(fuel_capacity)
        self._builder.set_fuel_efficiency(fuel_efficiency)
        self._builder.add_extra(extra) if extra else None
        return self._builder.create_new_vehicle()

    # def get_vehicle(self):
    #     return self.vehicle

