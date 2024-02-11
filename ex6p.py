processes=[]
n=int(input("enter no of processes"))
for i in range(n):
    process_id=int(input())
    arrival=int(input())
    burst=int(input())
    a=[process_id,arrival,burst]
    processes.append(a)
processes.sort(key=lambda x:x[1])
waiting_queue=[processes.pop(0)]
gantt_chart=[]
t=0
while True:
    if t==0:
        req=waiting_queue.pop(0)
        gantt_chart.append([req[0],t,t+1])
        t=t+1
        req[2]-=1
    else:
        if processes:
         if processes[0][1]==t:
            waiting_queue.append(processes.pop(0))
            waiting_queue.sort(key=lambda x:x[2])
            if req[2]==0:
                req=waiting_queue.pop(0)
                gantt_chart.append([req[0],t,t+1])
                t=t+1
                req[2]-=1
            else:
                if req[2]<waiting_queue[0][2]:
                    gantt_chart.append([req[0],t,t+1])
                    t=t+1
                    req[2]-=1
                else:
                    waiting_queue.append(req)
                    waiting_queue.sort(key=lambda x:x[2])
                    req=waiting_queue.pop(0)
                    gantt_chart.append([req[0],t,t+1])
                    t=t+1
                    req[2]-=1
         else:
             if req[2]==0:
                 req=waiting_queue.pop(0)
                 gantt_chart.append([req[0],t,t+1])
                 t+=1
                 req[2]-=1
             else:
                  if req[2]<waiting_queue[0][2]:
                    gantt_chart.append([req[0],t,t+1])
                    t=t+1
                    req[2]-=1
                  else:
                    waiting_queue.append(req)
                    waiting_queue.sort(key=lambda x:x[2])
                    req=waiting_queue.pop(0)
                    gantt_chart.append([req[0],t,t+1])
                    t=t+1
                    req[2]-=1
        else:
            for i in waiting_queue:
                gantt_chart.append([i[0],t,t+i[2]])
                t=t+i[2]
            break
print(gantt_chart)

