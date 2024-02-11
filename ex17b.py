capacity = int(input("Enter the capacity:"))

'''
n = int(input('Size:'))
processList = []
for i in range(n):
    val = int(input("Num:"))
    processList.append(val)
'''

processList = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
s = []
pageFaults = 0

for i in processList:
    if i not in s:
        if len(s) == capacity:
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pageFaults += 1
    else:
        s.remove(i)
        s.append(i)
    for j in s:
        print(j, end=" ")
    print()

ratio = pageFaults / (len(processList))
print('Number of misses:', pageFaults)
print('Miss ratio:', ratio)
print('Hit Ratio:', 1 - ratio)
