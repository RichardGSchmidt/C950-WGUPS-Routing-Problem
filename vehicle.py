
class Vehicle:
    def __init__(self, capacity, speed, load, packages, mileage, address, departure_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = departure_time
        self.time = departure_time


    def __str__(self):
        return print (f'{self.capacity}, {self.speed}, {self.load}, {self.packages}, {self.mileage}, {self.address}, {self.depart_time}')
