def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator"

    print("Result:", result)

while True:
    calculator()
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        break
