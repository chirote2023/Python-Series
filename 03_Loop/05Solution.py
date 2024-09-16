input_str = "teeterabcdbd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Result is : ",char)
        break
            