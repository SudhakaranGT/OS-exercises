def print_menu():
    print("\nEnter:")
    print("1. To add File")
    print("2. To Print Directory")
    print("3. To exit")

if __name__ == "__main__":
    num_blocks = int(input("Enter the number of Blocks in the disk: "))
    disk = [-1] * num_blocks
    file_map = {}
    map_idx = {}
    map_end_idx = {}
    tot_file = 0

    print("Welcome to the Sequential File")

    while True:
        print_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            file_name = input("Enter File name: ")
            start_block, total_blocks = map(int, input("Enter starting block and total number of blocks in the file: ").split())
            flag = 0

            for i in range(start_block, num_blocks):
                if disk[i] != -1:
                    break
                if start_block + total_blocks - 1 == i:
                    flag = 1
                    break

            if total_blocks == 0:
                flag = 0

            if flag == 1:
                occupied_blocks = [str(block) for block in range(start_block, start_block + total_blocks)]
                disk[start_block:start_block + total_blocks] = [tot_file] * total_blocks
                file_map[tot_file] = file_name
                map_idx[tot_file] = start_block
                map_end_idx[tot_file] = start_block + total_blocks - 1
                tot_file += 1
                print(f"File '{file_name}' allocated from block {start_block} to {start_block + total_blocks - 1}.")
            else:
                print("Something Went Wrong, either someone has occupied that space or out of bounds.")

        elif choice == 2:
            print("\n{:<15} {:<15} {:<15} {:<15}".format("File name", "Start Block", "End Block", "Blocks Occupied"))
            for i in range(tot_file):
                start_block = map_idx[i]
                end_block = map_end_idx[i]
                occupied_blocks = [str(block) for block in range(start_block, end_block + 1)]
                print("{:<15} {:<15} {:<15} {:<15}".format(file_map[i], start_block, end_block, ' - -> '.join(occupied_blocks)))

        elif choice == 3:
            break

        else:
            print("Invalid Input")
