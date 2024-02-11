import os

class File:
    def __init__(self, path):
        self.path = path

class Directory:
    def __init__(self, dname):
        self.dname = dname
        self.files = []

def create_directory(path, dname, files):
    directory_path = os.path.join(path, dname)
    os.makedirs(directory_path, exist_ok=True)
    directory = Directory(directory_path)
    for file in files:
        directory.files.append(file)
    return directory

def search_file(fname):
    matches = []
    for directory in directories:
        for file in directory.files:
            if fname in file.path:
                matches.append((directory.dname, file.path))
    if matches:
        print("\nMatch(es) found:")
        for directory_name, match in matches:
            print(f"In Directory '{directory_name}': {match}")

count = int(input("Enter the number of base directories: "))
directories = []

for _ in range(count):
    base_path = input("Enter the base directory path: ")
    dname = input("Enter the directory name: ")
    fcount = int(input("Enter the number of files in the directory: "))
    files = []
    for _ in range(fcount):
        path = input("Enter file path: ")
        files.append(File(path))
    directories.append(create_directory(base_path, dname, files))

search_key = input("Enter the file to search: ")
search_file(search_key)
