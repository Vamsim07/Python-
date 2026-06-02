Operator = input("Enter your Operation (+, -, *, /) : ")

num1 = int(input("Enter your 1st Number : "))
num2 = int(input("Enter Your 2nd Number : "))

if Operator == "+":
    print(num1 + num2)
elif Operator == "-":
    print(num1 - num2)
elif Operator == "*":
    print(num1 * num2)
elif Operator == "/":
    print(num1 / num2)
else:
    print("Enter Valid only Number")