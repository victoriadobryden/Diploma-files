import os
import random
import string


def create_random_file(file_size_mb):
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to bytes
    file_name = f"{file_size_mb}mb_file.txt"

    with open(file_name, 'w') as file:
        random_content = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size_bytes))
        file.write(random_content)

    print(f"File '{file_name}' created successfully.")


# Create files with different sizes
# file_sizes = [100, 300, 500, 700, 1000]  # Sizes in MB
file_sizes = [10, 20, 50, 80, 120]  # Sizes in MB

current_directory = os.getcwd()  # Get the current working directory

for size in file_sizes:
    file_path = os.path.join(current_directory, f"{size}mb_file.txt")
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists.")
    else:
        create_random_file(size)