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
    
# @ mean and staticmethod means is decoraters jo ki rules emplement karna ho, a method and use compulsory in uses like login page etc..

    @staticmethod
    def car_Desc():
        return "Luxury Cars is here."
       
# Inheritance
class FuelType(Car):
    def __init__(self, brand, model, fuelCapacity):
        super().__init__(brand, model)
        self.fuelCapacity = fuelCapacity
        
    def fuel_type(self):
        return "Electrical charge"
        
        

print(Car.car_Desc())
