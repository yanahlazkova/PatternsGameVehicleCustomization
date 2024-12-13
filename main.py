from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self):
        self.features = []

    def add_features(self, feature):
        self.features.append(feature)

    def __str__(self):
        return ", ".join(self.features)


class Builder(ABC):
    def __init__(self):
        self.vehicle = None

    def create_new_vehicle(self):
        self.vehicle = Vehicle()

    @abstractmethod
    def add_