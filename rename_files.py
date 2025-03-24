import os

# Define the directory containing files
directory = "test_files"

# Define the renaming pattern
prefix = "renamed_"

# Ensure the directory exists
if not os.path.exists(directory):
    print(f"❌ Error: Directory '{directory}' not found!")
    exit(1)

# Rename each file in the directory
for count, filename in enumerate(os.listdir(directory), start=1):
    old_path = os.path.join(directory, filename)
    
    # Skip directories, rename only files
    if os.path.isfile(old_path):
        new_name = f"{prefix}{count}.txt"
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_name}")

print("🎉 Renaming completed!")