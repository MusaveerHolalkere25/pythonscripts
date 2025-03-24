# Ask for the file name
file_name = input("Enter the file name: ")

try:
    # Open and read the file
    with open(file_name, "r") as file:
        content = file.read()

    # Count words
    word_count = len(content.split())

    # Print the word count
    print(f"✅ The file '{file_name}' contains {word_count} words.")

except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")