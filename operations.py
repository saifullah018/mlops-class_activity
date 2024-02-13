def square_number(x):
    """Returns the square of a number."""
    return x ** 2

def greet(name):
    """Greets the user."""
    return f"Hello, {name}! Welcome to the Python world."

# Example usage:
number = 5
print(f"The square of {number} is: {square_number(number)}")

username = input("Enter your name: ")
print(greet(username))
