number = int(input("Enter the number : "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i ) ==0:
            is_prime = False
            break
        
print("Prime number is : ",is_prime)