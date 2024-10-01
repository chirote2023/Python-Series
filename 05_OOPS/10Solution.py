# Multiply Inheritance

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        
class Battery:
    def Batter_info(self):
        return "This is Battery"


class Engine:
    def Engine_info(self):
        return "This is Engine"

class Electrical_Car(Battery, Engine,Car):
    pass

my_new_car = Electrical_Car("TATA" , "Safari")
print(my_new_car.Batter_info())
print(my_new_car.Engine_info())