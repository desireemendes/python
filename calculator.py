# num1 = input("Enter a number ")
# num2 = input("Enter another number ")

#can use int or float to convert to numbers
# result = float(num1) + float(num2)
# print(result)


num1 = float(input("Enter a number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter another number: "))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
  print(num1 / num2)
elif operator == "*":
  print(num1 * num2)
else:
  print("Invalid operator")