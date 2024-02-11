import subprocess

# Command 1: ls (List files in a directory)
option1 = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)
option2 = subprocess.run(["ls", "-a"], stdout=subprocess.PIPE, text=True)

print("Option 1 - List files in long format:")
print(option1.stdout)

print("Option 2 - List all files (including hidden):")
print(option2.stdout)

# Command 2: cp (Copy a file)
source_file = "source.txt"
destination_file = "destination.txt"

subprocess.run(["cp", source_file, destination_file])

print(f"File '{source_file}' copied to '{destination_file}'")

# Command 3: cat (Display file contents)
file_to_display = "source.txt"

option1 = subprocess.run(["cat", file_to_display], stdout=subprocess.PIPE, text=True)
option2 = subprocess.run(["cat", "-n", file_to_display], stdout=subprocess.PIPE, text=True)

print("Option 1 - Display file contents:")
print(option1.stdout)

print("Option 2 - Display file contents with line numbers:")
print(option2.stdout)

# Command 4: mv (Move or rename a file)
source_file = "source.txt"
destination_file = "newfile.txt"

subprocess.run(["mv", source_file, destination_file])

print(f"File '{source_file}' moved/renamed to '{destination_file}'")

# Command 5: grep (Search for a pattern in a file)
file_to_search = "newfile.txt"
pattern = "Hello"

option1 = subprocess.run(["grep", pattern, file_to_search], stdout=subprocess.PIPE, text=True)
option2 = subprocess.run(["grep", "-i", pattern, file_to_search], stdout=subprocess.PIPE, text=True)

print("Option 1 - Search for 'example' in the file:")
print(option1.stdout)

print("Option 2 - Search for 'example' (case-insensitive) in the file:")
print(option2.stdout)

