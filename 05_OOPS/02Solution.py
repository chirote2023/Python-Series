class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_Name(self):
        return f"{self.brand} {self.model}"
        
        
my_car = Car("TATA MOTORS" ,"Safari-Black" )
my_new_car = Car("KIA" ,"Seltos" )

print(my_car.full_Name())
# print(my_car.model)
print(my_new_car.full_Name())
# print(my_new_car.model)