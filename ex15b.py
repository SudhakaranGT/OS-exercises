def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("Process No.    Process Size     Block no.")
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
    bestFit(blocksize, m, processSize, n)
