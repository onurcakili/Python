"""
PROJECT: Simple Calculator
===========================
Level: Beginner
Author: Onur Çakılı
Description: A command-line calculator with basic operations
"""

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    """Calculate x to the power of y"""
    return x ** y

def modulus(x, y):
    """Calculate modulus"""
    if y == 0:
        return "Error: Division by zero!"
    return x % y

def display_menu():
    """Display calculator menu"""
    print("\n" + "=" * 40)
    print("SIMPLE CALCULATOR")
    print("=" * 40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("=" * 40)

def get_numbers():
    """Get two numbers from user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")
        return None, None

def calculate(choice, num1, num2):
    """Perform calculation based on choice"""
    operations = {
        '1': (add, '+'),
        '2': (subtract, '-'),
        '3': (multiply, '*'),
        '4': (divide, '/'),
        '5': (power, '^'),
        '6': (modulus, '%')
    }
    
    if choice in operations:
        operation, symbol = operations[choice]
        result = operation(num1, num2)
        
        if isinstance(result, str):  # Error message
            print(f"\n{result}")
        else:
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
            return result
    else:
        print("\nError: Invalid choice!")
    
    return None

def main():
    """Main calculator function"""
    print("\nWelcome to Simple Calculator!")
    history = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("\nCalculator History:")
            if history:
                for i, calc in enumerate(history, 1):
                    print(f"{i}. {calc}")
            else:
                print("No calculations performed.")
            print("\nThank you for using the calculator!")
            break
        
        num1, num2 = get_numbers()
        
        if num1 is not None and num2 is not None:
            result = calculate(choice, num1, num2)
            if result is not None:
                history.append(f"{num1} {['', '+', '-', '*', '/', '^', '%'][int(choice)]} {num2} = {result}")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Demo mode (comment out for interactive mode)
    print("=" * 40)
    print("CALCULATOR DEMO")
    print("=" * 40)
    
    # Test all operations
    test_cases = [
        (10, 5, add, "Addition"),
        (10, 5, subtract, "Subtraction"),
        (10, 5, multiply, "Multiplication"),
        (10, 5, divide, "Division"),
        (2, 3, power, "Power"),
        (10, 3, modulus, "Modulus")
    ]
    
    for num1, num2, operation, name in test_cases:
        result = operation(num1, num2)
        print(f"{name}: {num1} and {num2} = {result}")
    
    # Test error handling
    print(f"\nDivision by zero: {divide(10, 0)}")
    print(f"Modulus by zero: {modulus(10, 0)}")
    
    print("\n" + "=" * 40)
    print("DEMO COMPLETED!")
    print("=" * 40)
    
    # Uncomment below to run interactive mode
    # main()
