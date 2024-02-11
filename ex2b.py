import os

def file_operations(filename):
    try:
        fd = os.open(filename, os.O_RDWR)
        if fd:
            os.write(fd, b"This is a sample text.")
            os.lseek(fd, 0, os.SEEK_SET)
            data = os.read(fd, 1024)
            print("Read data:", data.decode())
            os.close(fd)
        else:
            print("Error opening file")
    except OSError as e:
        print("File operation error:", e)

def main():
    filename = "sample.txt"
    file_operations(filename)

if __name__ == "__main__":
    main()
