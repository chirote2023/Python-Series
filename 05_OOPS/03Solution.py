class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_Name(self):
        return f"{self.brand} {self.model} {self.fuelCapacity}"
        
# Inheritance
class FuelCapacity(Car):
    def __init__(self, brand, model, fuelCapacity):
        super().__init__(brand, model)
        self.fuelCapacity = fuelCapacity
        

my_car = FuelCapacity("TATA MOTORS" ,"Safari-Black","50L" )
print(my_car.full_Name())


# Inheritance means jo dada ka hai wo papa ka or fir mera bhi 