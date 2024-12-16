from vehicle import Vehicle


class ExternalVehicleAdapter:
    def __init__(self, external_data):
        self.external_data = external_data

    def to_internal_format(self):
        vehicle_type = self.external_data['vehicle_type']
        specs = self.external_data['specs']
        extras = self.external_data.get('extras', [])
        return Vehicle(
            vehicle_type=vehicle_type,
            max_speed=specs['speed'],
            fuel_capacity=specs['fuel_capacity'],
            fuel_efficiency=specs['fuel_efficiency'],
            extras=extras,
        )
