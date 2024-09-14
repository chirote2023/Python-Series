Distance = int(input("Enter your distance : "))

if Distance < 3:
    print("Walk")
    
elif Distance <= 15:
    print("Bike")
    
else:
    print("Car")