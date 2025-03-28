def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get user input
try:
    num = int(input("Enter a number: "))

    # Check if it's prime and print the result
    if is_prime(num):
        print(f"✅ {num} is a prime number.")
    else:
        print(f"❌ {num} is not a prime number.")

except ValueError:
    print("❌ Please enter a valid integer.")