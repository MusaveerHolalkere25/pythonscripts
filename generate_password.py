import secrets
import string

def generate_password(length=12):
    # Define the character set: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Generate and print a random password
print(f"🔐 Your secure password: {generate_password()}")