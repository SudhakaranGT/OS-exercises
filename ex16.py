import random

class PageTable:
    def __init__(self, physical_size, logical_size, page_size, starting_addr):
        self.frames = physical_size // page_size
        self.pages = logical_size // page_size
        self.page_size = page_size
        self.start = starting_addr
        self.table = []

    def create_table(self):
        for i in range(self.frames):
            if i == 0:
                self.table.append([i, -1, self.start])
            else:
                self.table.append([i, -1, self.table[-1][-1] + self.page_size])

    def map_table(self, page):
        free = []
        for i in range(len(self.table)):
            if self.table[i][1] == -1:
                free.append(i)
        choice = random.choice(free)
        self.table[choice][1] = page

physical_size = int(input('Enter the Physical Address Size: '))
logical_size = int(input('Enter the Logical Address Size: '))
page_size = int(input('Enter the Page Size: '))
starting_addr = int(input('Enter the Starting Address: '))

page_table = PageTable(physical_size, logical_size, page_size, starting_addr)
page_table.create_table()

print("Before allocation...")
print("Frame Number\tPage Number\tStarting Address")
for entry in page_table.table:
    print(f"{entry[0]}\t\t{entry[1]}\t\t{entry[2]}")

for i in range(page_table.pages):
    page_table.map_table(i)

print("After allocation...")
print("Frame Number\tPage Number\tStarting Address")   
for entry in page_table.table:
    print(f"{entry[0]}\t\t{entry[1]}\t\t{entry[2]}")

logical_addr = int(input("Enter address between 0 to 15: "))
page = logical_addr // page_table.pages
offset = logical_addr % page_table.pages

for entry in page_table.table:
    if entry[1] == page:
        physical_address = entry[2] + offset
        break

print("Physical address:", physical_address)
