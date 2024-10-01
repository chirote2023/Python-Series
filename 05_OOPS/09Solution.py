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
print(isinstance(tesla,Car))
print(isinstance(tesla,FuelType))


# isinsatance is key word to check to tesla car or electrical (true or false) value answer.