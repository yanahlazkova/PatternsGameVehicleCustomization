from vehicleAdapter import ExternalVehicleAdapter
import vehicle
from vehicleFactory import VehicleFactory

car_builder = vehicle.CarBuilder()
director = vehicle.Director(car_builder)
new_car = director.construct_vehicle(200,
                                     100,
                                     5,
                                     ["GPS", "Climate Control"])
print(new_car)

external_data = {
    "vehicle_type": "Truck",
    "specs": {
        "speed": 80,
        "fuel_capacity": 150,
        "fuel_efficiency": 15
    },
    "extras": ["Trailer", "Enhanced Engine"]
}

vehicle_data = ExternalVehicleAdapter(external_data)
new_vehicle = vehicle_data.to_internal_format()
print(new_vehicle)

car = ('Car', 200, 100, 5, ["GPS", "Climate Control"])
truck = ('Truck', 80, 150, 15, ["Trailer", "Enhanced Engine"])
pickup = ('Pickup', 80, 150, 15, ["Trailer", "Enhanced Engine"])
plan_list = [car, truck, pickup]
for item in plan_list:
    vehicle = VehicleFactory.build_car(item)
    print(vehicle)
