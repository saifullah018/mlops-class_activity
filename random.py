import random

def roll_dice():
    """Simulates rolling a six-sided dice."""
    return random.randint(1, 6)

def generate_password(length=8):
    """Generates a random password of given length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

def shuffle_list(lst):
    """Shuffles the elements of a list."""
    shuffled_list = lst[:]
    random.shuffle(shuffled_list)
    return shuffled_list

# Example usage:
print("Rolling the dice:", roll_dice())

print("Generated Password:", generate_password())

my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
print("Shuffled List:", shuffle_list(my_list))
