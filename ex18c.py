class Node:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.next = None
        self.down = None
        self.content = None 

def new_node(item, type1, content=None):
    temp = Node(item, type1)    
    temp.next = None
    temp.down = None
    temp.content = content
    return temp


def inorder(root, p):
    if root.next != None and root.name != p:
        inorder(root.next, p)
        print(root.name)
        if root.type == 1:
            inorder(root.down, p)
    return root

def find(node, key):
    if node is not None:
        if node.name == key:
            print(f"Found {node.name}")
            return node
        else:
            found_node = find(node.down, key)
            if found_node is None:
                found_node = find(node.next, key)
            return found_node
    return None


def insert(node, key, par, mode, content=None):
    if node is None:
        print("The root node is getting created.....")
        return new_node(key, mode, content)
    else:
        temp = None
        temp = inorder(node, par)
        temp1 = new_node(key, mode, content)  # Pass content parameter here
        if temp.down is None and temp.type == 1:
            temp.down = temp1
            if temp1.type == 2:
                print(f"File {temp1.name} successfully inserted")
            else:
                print(f"Directory {temp1.name} successfully inserted")
        else:
            temp = temp.down
            while temp.next is not None:
                temp = temp.next
            temp.next = temp1
            if temp1.type == 2:
                print(f"File {temp1.name} successfully inserted")
            else:
                print(f"Directory {temp1.name} successfully inserted")
    return node

root = None
c = 0
p = 0
parent = [None] * 50
child = [None] * 50
cont = 'y'
root = insert(root, "root", "", 1)
while cont == 'y':
    par_dir = input("Enter parent directory: ")
    t = int(input("Enter type (1 for directory and 2 for file): "))
    file_or_dir = input("Enter directory or file name: ")


    # Ask for file contents if it's a file
    content = None
    if t == 2:
        content = input("Enter file contents: ")

    insert(root, file_or_dir, par_dir, t, content)

    child[c] = file_or_dir
    parent[p] = par_dir
    c += 1
    p += 1
    cont = input("Wanna insert more? (y/n): ")
    

finder = input("Enter file name/directory name to search: ")
found_node = find(root, finder)

if found_node:
    option = input("Do you want to display file content? (y/n): ")
    if found_node.content==None:
        print("It's a directory")
   
    elif option.lower() == 'y' and found_node.type == 2 and found_node.content:
        print(f"File content of {found_node.name}: {found_node.content}")
    
        par = ""
        chi = found_node.name
        print("The path in reverse order is")
        while par != "root":
            for i in range(c):
                if child[i] == chi:
                    par = parent[i]
                    chi = parent[i]
                    print(par)
                    break




