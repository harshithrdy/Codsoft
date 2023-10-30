# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator program
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    user_choice = input(": ")

    if user_choice == "quit":
        break

    if user_choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_choice == "add":
            result = add(num1, num2)
        elif user_choice == "subtract":
            result = subtract(num1, num2)
        elif user_choice == "multiply":
            result = multiply(num1, num2)
        elif user_choice == "divide":
            result = divide(num1, num2)

        print("Result: ", result)
    else:
        print("Invalid input. Please try again.")
