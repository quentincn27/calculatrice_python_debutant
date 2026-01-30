print("My first calculator in Python!")

# ask the user to choose two numbers
number1 = input("Enter a number: ")
number2 = input("Enter a second number: ")

# check whether both inputs are numeric
if number1.isnumeric() and number2.isnumeric():
    print("You have correctly entered two numbers!")

# otherwise, the inputs are not numbers and the program stops
else:
    print("At least one of the entered values is not a number")
    raise SystemExit("End of program")

# inputs are numbers: convert from string to int
number1 = int(number1)
number2 = int(number2)

# ask the user to choose a calculation method
operation = input(
    "Do you want to subtract, add, multiply, or divide? (type -, +, *, /): "
)

# check that the user chose a valid operator
if operation not in ["-", "+", "*", "/"]:
    print("You did not choose a valid operation!")
    raise SystemExit("End of program")

# perform the calculation
else:
    if operation == "-":
        result = number1 - number2
    elif operation == "+":
        result = number1 + number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        # prevent division by zero
        if number2 == 0:
            print("Division by zero is not allowed!")
            raise SystemExit("End of program")
        else:
            result = number1 / number2

    print(result)

input("Press Enter to exit...")
