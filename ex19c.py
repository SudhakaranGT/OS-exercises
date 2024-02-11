def print_menu():
    print("Enter:")
    print("1. To add File")
    print("2. To Print Directory")
    print("3. To exit")


if __name__ == "__main__":
    num_block = int(input("Enter the number of blocks in the disk: "))
    disk = [-1] * num_block
    arr = [[None] * 100000 for _ in range(1000)]
    file_map = [None] * 100000
    map_idx = [0] * 100000
    sz = [0] * 100000
    tot_file = 0

    print("Welcome to the indexed File")

    while True:
        print_menu()
        choice = int(input())

        if choice == 1:
            file_name, i_block, t_block = input("Enter File name, indexed block, and total number of blocks in the file: ").split()
            i_block, t_block = int(i_block), int(t_block)

            if i_block < 0 or i_block >= num_block or disk[i_block] != -1:
                print("Index Block is not empty or invalid")
                continue

            free_block = []
            j = 0
            cnt = 0
            disk[i_block] = tot_file

            for i in range(t_block):
                while j < num_block:
                    if disk[j] == -1:
                        free_block.append(j)
                        cnt += 1
                        j += 1
                        break
                    j += 1

            if cnt == t_block:
                for i in range(t_block):
                    arr[tot_file][i] = free_block[i]  # Store free block index
                    disk[free_block[i]] = tot_file
                print()
                file_map[tot_file] = file_name
                map_idx[tot_file] = i_block
                sz[tot_file] = t_block
                tot_file += 1
            else:
                disk[i_block] = -1
                print("Not Enough free Space")

        elif choice == 2:
            print("File name      Index Block    Block Stored")
            for i in range(tot_file):
                print(f"{file_map[i]:<16} {map_idx[i]:<16}", end="")
                for j in range(sz[i]):
                    print(f"{arr[i][j]}", end="")
                    if j < sz[i] - 1:
                        print(" --> ", end="")
                print()

        elif choice == 3:
            break

        else:
            print("Invalid Input")
