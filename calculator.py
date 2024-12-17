#Calculator app
symbols = ["+","-","*","/"]

while True:
    calculation = input("Enter the symbol for calculation(+,-,*,/): ")
    if calculation in symbols:
        break
    else:
        print("Invalid operation.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if calculation in ["+","-","*","/"]:
    if calculation == "+":
        print("Sum is:",num1 + num2)
    elif calculation == "-":
        print("Difference is: ", num1 - num2)
    elif calculation == "*":
        print("Product is: ", num1*num2)
    elif calculation == "/":
        print("Division is: ", num1/num2)
    else:
        pass