def calculator():
    while True:
        # Get user input
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Check if inputs are valid numbers
        if not are_valid_numbers(num1, num2):
            print("Your inputs are not valid.")
            continue
        
        # Convert the inputs to numbers
        num1 = float(num1)
        num2 = float(num2)

        operation = input("Enter operation (+, -, /, *): ")

        # Check if operation is valid
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation")
            continue  # Proceed to the next iteration

        # Perform the calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Can't divide by zero.")
                continue  # Proceed to the next iteration
            else:
                result = num1 / num2
        
        # Display the result
        print("Result:", result)

        # Ask for another calculation
        repeat = input("Do you want to perform another calculation? (y/n): ")
        if repeat.lower() == 'n':
            break

def are_valid_numbers(num1, num2):
    try:
        # Try to convert the inputs to numbers
        float(num1)
        float(num2)
        return True  # If successful, return True
    except ValueError:
        return False  # If conversion fails, return False

calculator()
