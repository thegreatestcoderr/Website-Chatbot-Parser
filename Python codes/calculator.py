result = 0
value1 = input("Enter first number: ")
value1 = int(value1)
value2 = input("Enter second nubmer: ")
value2 = int(value2)
print("Enter Type of Operation")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
operator = input("Enter type of operation (addition, subtraction, multiplication, division): ")
operator = int(operator)
if operator==1:
    print(value1 + value2)
elif operator==2:
    print(value1 - value2)
elif operator==3:
    print(value1 * value2)
elif operator==4:
    print(value1/value2)
else:
    print("invalid")
