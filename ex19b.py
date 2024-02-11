import random

class Node:
    def __init__(self, val):
        self.ptr = None
        self.val = val

arr = [None] * 100
fileMap = [None] * 100
mapIdx = [0] * 100
sz = [0] * 100

def printMenu():
    print("Enter:")
    print("1. To add File")
    print("2. To Print Directory")
    print("3. To exit")

def main():
    numBlock = int(input("Enter the number of Blocks in the disk: "))
    disk = [-1] * numBlock
    totFile = 0
    file = []
    blocks = []
    count = 0

    while True:
        printMenu()
        choice = int(input())

        if choice == 1:
            fName = input("Enter File name: ")

            if fName in file:
                print("File already exists")
                continue

            sBlock = int(input("Enter the starting block: "))

            if sBlock < 0 or sBlock >= numBlock or disk[sBlock] != -1:
                print("Start Block is not empty or invalid")
                continue

            tBlock = int(input("Enter the total number of blocks in the file: "))

            if count > numBlock:
                print("Enter a valid number of blocks!")
                continue

            file.append(fName)
            freeBlock = [sBlock]
            blocks.append(sBlock)

            for _ in range(tBlock - 1):
                while True:
                    randomBlock = random.randint(0, numBlock - 1)
                    if disk[randomBlock] == -1 and randomBlock not in disk and randomBlock not in blocks:
                        freeBlock.append(randomBlock)
                        disk[randomBlock] = totFile
                        count += 1
                        blocks.append(randomBlock)
                        break

            head = None

            for block in freeBlock:
                idx = Node(block)
                idx.ptr = None
                if head is None:
                    arr[totFile] = idx
                    head = idx
                else:
                    head.ptr = idx
                    head = idx

            fileMap[totFile] = fName
            sz[totFile] = tBlock
            totFile += 1

            if count == numBlock:
                break

        elif choice == 2:
            print("File name Block Stored")
            for i in range(totFile):
                print(f"{fileMap[i]} ", end="")
                head = arr[i]
                while head is not None:
                    print(f"{head.val} ->", end="")
                    head = head.ptr
                print("NULL")

        elif choice == 3:
            break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
