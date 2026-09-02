# Basic Python program with input validation and error handling

def get_number(prompt):
    """Safely get a float number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=== Simple Calculator ===")
    
    # Get two numbers from the user
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    # Perform calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # Handle division by zero
    try:
        division = num1 / num2
    except ZeroDivisionError:
        division = "Undefined (division by zero)"

    # Display results
    print("\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

if __name__ == "__main__":
    main()

