"""
Main module for the Python project.
"""

def greet(name: str) -> str:
    """
    Return a greeting message.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to my Python project."

def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of the two numbers
    """
    return a + b

if __name__ == "__main__":
    import sys
    
    print(greet("My name is Kahaan"))
    
    # Get numbers from command line arguments, default to 3 and 3
    if len(sys.argv) >= 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers as arguments")
            sys.exit(1)
    else:
        num1, num2 = 3, 3  # Default values
    
    print(f"{num1} + {num2} = {add_numbers(num1, num2)}") 