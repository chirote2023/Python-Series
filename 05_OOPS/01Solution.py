class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        
my_car = Car("TATA MOTORS" ,"Safari-Black" )
my_new_car = Car("KIA" ,"Seltos" )

print(my_car.brand)
print(my_car.model)
print(my_new_car.brand)
print(my_new_car.model)