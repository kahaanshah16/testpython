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
    print(greet("World"))
    print(f"3 + 3 = {add_numbers(2, 3)}") 