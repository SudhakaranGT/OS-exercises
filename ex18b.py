import os

class File:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

class UserDirectory:
    def __init__(self, path):
        self.path = path
        self.files = {}

def create_user_directory(system, master_directory, username):
    # Create a new user directory for the given username.
    if username not in system.master_directory:
        user_path = os.path.join(master_directory, username)
        os.makedirs(user_path, exist_ok=True)
        system.master_directory[username] = UserDirectory(user_path)

def create_new_file_in_user_directory(system, username, filename, content):
    # Create a new file with content in the user's directory.
    if username in system.master_directory:
        user_directory = system.master_directory[username]
        file_path = os.path.join(user_directory.path, filename)
        with open(file_path, 'w') as file:
            file.write(content)
        user_directory.files[filename] = File(filename, content)
    else:
        print(f"User '{username}' not found. Create the user directory first.")

def list_user_files(system, username):
    # List the files in the user's directory.
    if username in system.master_directory:
        user_directory = system.master_directory[username]
        print(f"Files in User '{username}' Directory:")
        for filename in user_directory.files:
            print(filename)

def read_file(system, username, filename):
    # Read the content of a file in the user's directory.
    if username in system.master_directory:
        user_directory = system.master_directory[username]
        if filename in user_directory.files:
            file = user_directory.files[filename]
            return file.content
        else:
            return f"File '{filename}' not found in User '{username}' Directory."
    else:
        return f"User '{username}' not found."

class TwoLevelDirectorySystem:
    def __init__(self):
        # The master directory, a dictionary with usernames as keys and user directories as values.
        self.master_directory = {}

master_directory_path = input("Enter the path where the master directory should be created:")
if not os.path.exists(master_directory_path):
    os.makedirs(master_directory_path)

system = TwoLevelDirectorySystem()

while True:
    print("\nOptions:")
    print("1. Create User Directory")
    print("2. Create New File in User Directory")
    print("3. List User Files")
    print("4. Read File Content")
    print("5. Exit")

    choice = input("Enter your choice:")
    
    if choice == '1':
        username = input("Enter the username:")
        create_user_directory(system, master_directory_path, username)
    elif choice == '2':
        username = input("Enter the username:")
        filename = input("Enter the filename:")
        content = input("Enter the content for the new file:")
        create_new_file_in_user_directory(system, username, filename, content)
    elif choice == '3':
        username = input("Enter the username:")
        list_user_files(system, username)
    elif choice == '4':
        username = input("Enter the username:")
        filename = input("Enter the filename:")
        content = read_file(system, username, filename)
        print(content)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
