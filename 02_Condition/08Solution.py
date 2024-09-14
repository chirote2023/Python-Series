Password_checker = int(input("Enter your Password : "))

if Password_checker <= 6:
    print("Week")
elif Password_checker <= 10:
    print("Medium")
elif Password_checker <= 15 :
    print("Strong")
else:
    print("Strong")