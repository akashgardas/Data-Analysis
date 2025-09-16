class Vehicle:
    def __init__(self, license: str, plate: str, owner_name: str, fee_per_hour: int=20):
        self.license = license
        self.plate = plate
        self.owner_name = owner_name
        self.fee_per_hour = fee_per_hour
        self.parking_spot = None
    
    def display(self):
        print(f'License: {self.license}')
        print(f'Plate: {self.plate}')
        print(f'Owner Name: {self.owner_name}')
        print(f'Spot Status: {self.spot_status}')
    
    def calc_parking_fee(self, hours=1):
        return hours * self.fee_per_hour
    

class Bike(Vehicle):
    def __init__(self, license, plate, owner_name, helmet_req, fee_per_hour=20):
        super().__init__(license, plate, owner_name, fee_per_hour)
        self.helmet_req = helmet_req
        
    def display(self):
        super().display()
        print(f'Helmet Required: {self.helmet_req}')


class Car(Vehicle):
    def __init__(self, license, plate, owner_name, seats, fee_per_hour=50):
        super().__init__(license, plate, owner_name, fee_per_hour)
        self.seats = seats
    
    def display(self):
        super().display()
        print(f'Seats: {self.seats}')


class SUV(Vehicle):
    def __init__(self, license, plate, owner_name, four_wheel_drive, fee_per_hour=70):
        super().__init__(license, plate, owner_name, fee_per_hour)
        self.four_wheel_drive = four_wheel_drive
    
    def display(self):
        super().display()
        print(f'Four Wheel Drive: {self.four_wheel_drive}')


class Truck(Vehicle):
    def __init__(self, license, plate, owner_name, max_load_capacity, fee_per_hour=100):
        super().__init__(license, plate, owner_name, fee_per_hour)
        self.max_load_capacity = max_load_capacity
        
    def display(self):
        super().display()
        print(f'Max Load Capacity: {self.max_load_capacity}')
