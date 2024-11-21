# Welcome to the Python Calculator! 🎉
# Complete the code to add operations like addition, subtraction, multiplication, and modulus.

def calculate(a, b, operation):
    if operation == "add":
        return a + b
        pass
    elif operation == "subtract":
        # Add your logic here
        return a - b
        pass
    elif operation == "multiply":
        # Add your logic here
        pass
    elif operation == "modulus":
        # Add your logic here
        pass
    else:
        return "Operation not supported!"

if __name__ == "__main__":
    print("Welcome to the Python Calculator!")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Enter the operation (add, subtract, multiply, modulus): ")
    result = calculate(num1, num2, op)
    print(f"The result is: {result}")
