dir = {
    'dname': '',
    'files': {}
}

dir['fcnt'] = 0
dir['dname'] = input("Enter name of directory -- ")

while True:
    print("\n\n 1. Create File\t2. Delete File\t3. Search File \n 4. Display Files\t5. Display file content\t6. Exit")
    ch = int(input("Enter your choice -- "))

    if ch == 1:
        fname = input("\n Enter the name of the file -- ")
        content = input("Enter file contents --")
        dir['files'][fname] = content

    elif ch == 2:
        f = input("\n Enter the name of the file -- ")
        if f in dir['files']:
            del dir['files'][f]
            print("File", f, "found and deleted")
        else:
            print("File", f, "not found")
            dir['fcnt'] -= 1

    elif ch == 3:
        f = input("\n Enter the name of the file -- ")
        if f in dir['files']:
            print("File", f, "found")
        else:
            print("File", f, "not found")

    elif ch == 4:
        if len(dir['files']) == 0:
            print("\n Directory Empty")
        else:
            print("\n The Files are -- ")
            for i in dir['files']:
                print(i, end="\n")

    elif ch == 5:
        f = input("\n Enter the name of the file -- ")
        if f in dir['files']:
            print("Content:")
            print(dir['files'][f])
        else:
            print("File not found")

    else:
        print("Invalid option!!")
        break
