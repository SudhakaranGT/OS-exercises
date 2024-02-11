def worstFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]
    print("Process No. Process Size Block no.")
    for i in range(n):
        print(i + 1, " ", processSize[i], end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blocksize = []
    processSize = []
    m = int(input("Enter the number of blocks: "))
    for i in range(m):
        s = int(input("Enter the size of the block: "))
        blocksize.append(s)
    n = int(input("Enter the number of processes: "))
    for i in range(n):
        s = int(input("Enter the size of process: "))
        processSize.append(s)
    worstFit(blocksize, m, processSize, n)
