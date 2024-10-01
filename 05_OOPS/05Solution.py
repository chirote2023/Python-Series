#Polymorphism wo hoto hai jo ek or anake roupe hote hai for ex. + number ko bhi add karta hai or string ko bhi add karta hai.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    #Encapulation
    def get_brand(self):
        return self.__brand + " !"
        
    def full_Name(self):
        return f"{self.__brand} {self.model} {self.fuelCapacity}"
    
    
    def fuel_type(self):
        return "Petrol or Disel"
    
    
        
# Inheritance
class FuelType(Car):
    def __init__(self, brand, model, fuelCapacity):
        super().__init__(brand, model)
        self.fuelCapacity = fuelCapacity
        
    def fuel_type(self):
        return "Electrical charge"
        
        
tesla = Car("TATA MOTORS" ,"Safari-Black")
print(tesla.fuel_type())

my_car = FuelType("Tesla","model S", "85KWh")
print(my_car.fuel_type())
