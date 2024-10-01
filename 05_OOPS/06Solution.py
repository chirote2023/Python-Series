class Car:
    # Class variable declare in global scope and access in local scope.
    
    total_car = 0
     
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
        
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
        
        
Car("TATA MOTORS" ,"Safari-Black")
Car("TATA MOTORS","Nexon")
Car("TATA MOTORS","Tiago")
Car("TATA MOTORS","Altraz")
Car("KIA", "Seltos")
Car("KIA", "Sonet")
Car("KIA", "Carnival")
Car("Tesla","model S")

print("Totla No. of Cars : ",Car.total_car)
