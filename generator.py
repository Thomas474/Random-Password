import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!_?"

    # Combine all characters
    all_chars = letters + digits + special_chars

    # Ensure the password has:
    # - At least one letter
    # - Exactly 4 numbers
    # - At least one special character
    password = [
        random.choice(letters),  # At least one letter
        random.choice(special_chars)  # At least one special character
    ]

    # Add exactly 4 numbers
    for _ in range(4):
        password.append(random.choice(digits))

    # Fill the rest of the password with random choices
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))

    # Shuffle the password to mix the characters
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

# Generate and print a password
print("Your random password is:", generate_password())