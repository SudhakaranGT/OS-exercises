processes=[]
n=int(input("enter no of processes"))
for i in range(n):
    a=list(map(int,input().split()))
    processes.append(a)

processes.sort(key=lambda x:x[1])
gantt_chart=[]
t=0

waiting_queue=[]

if processes[0][1]!=0:
    req=processes[0][1]
    t=processes[0][1]
    for i in range(len(processes)):
        if processes[i][1]==req:
            waiting_queue.append(processes[i])
            processes[i]=False
    waiting_queue.sort(key=lambda x:x[2])

else:
    for i in range(len(processes)):
        if processes[i][1]==0:
            waiting_queue.append(processes[i])
            processes[i]=False
    waiting_queue.sort(key=lambda x:x[2])

while True:
    all_false = all(item == False for item in processes)

    if not all_false:
        req=waiting_queue.pop(0)
        gantt_chart.append([req[0],t,t+req[2]])
        for i in range(len(processes)):
          if processes[i]:
            if processes[i][1]>=t and processes[i][1]<=t+req[2]:
                waiting_queue.append(processes[i])
                processes[i]=False
        t=t+req[2]
        waiting_queue.sort(key=lambda x:x[2])

    else:
        for i in waiting_queue:
            gantt_chart.append([i[0],t,t+i[2]])
            t=t+i[2]
        break
    
print(gantt_chart)


