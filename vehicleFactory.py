import vehicle


class VehicleFactory:
    @staticmethod
    def build_car(plan) -> vehicle.Vehicle:
        plan_type, speed, capacity, efficiency, extra = plan
        list_type = {
            'Car': vehicle.CarBuilder,
            'Motorcycle': vehicle.MotorcycleBuilder,
            'Truck': vehicle.TruckBuilder,
        }
        try:
            if plan_type not in list_type:
                raise AssertionError(f"Vehicle type '{plan_type}' is not valid")

            vehicle_builder = list_type[plan_type]()
            director = vehicle.Director(vehicle_builder)
            return director.construct_vehicle(speed, capacity,efficiency,extra)

        except AssertionError as e:
            print(e)
