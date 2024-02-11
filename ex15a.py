def firstFit(blockSize, bs, processSize, ps):
    allocation = [-1] * ps
    for i in range(ps):
        for j in range(bs):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break
    print(" Process No. Process Size Block no.")
    for i in range(ps):
        print(" ", i + 1, " ", processSize[i], " ", end=" ")
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
    firstFit(blocksize, m, processSize, n)
'''
io
5
100
500
200
300
600
4
212
417
112
426
'''