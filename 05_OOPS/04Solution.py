class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    #Encapulation me function ke under access le sakte hai or global lena hoto method ko call karna padta hai for ex: line no. 23 and encapulation private rehta hai.
    def get_brand(self):
        return self.__brand + " !"
        
    def full_Name(self):
        return f"{self.__brand} {self.model} {self.fuelCapacity}"
        
# Inheritance
class FuelCapacity(Car):
    def __init__(self, brand, model, fuelCapacity):
        super().__init__(brand, model)
        self.fuelCapacity = fuelCapacity
        

my_car = FuelCapacity("TATA MOTORS" ,"Safari-Black","50L" )
# print(my_car.full_Name())

print(my_car.get_brand())