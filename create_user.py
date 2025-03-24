import subprocess

def create_user(username):
    """Creates a Linux user and verifies the creation."""

    # Check if the user already exists
    try:
        subprocess.run(["id", username], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ User '{username}' already exists.")
        return
    except subprocess.CalledProcessError:
        pass  # User does not exist, continue to create

    # Create the user
    try:
        subprocess.run(["sudo", "useradd", "-m", "-s", "/bin/bash", username], check=True)
        print(f"✅ User '{username}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to create user '{username}'. Ensure you have sudo privileges.")
        return

    # Verify user creation
    try:
        subprocess.run(["id", username], check=True)
        print(f"✅ Verification successful: '{username}' exists in the system.")
    except subprocess.CalledProcessError:
        print(f"❌ Verification failed: '{username}' does not exist.")

# Get username input from the user
username = input("Enter the username to create: ")
create_user(username)