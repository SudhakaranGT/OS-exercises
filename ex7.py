def nonpreemptive(d): 
    queue = []
    d = dict((sorted(d.items(), key=lambda x:x[1])))
    for k, v in d.items():
        for i in range(v[1]): # print(k)
            d = dict(sorted(d.items(), key=lambda x:x[1][2])) # print(d)
        for k,v in d.items():
            for i in range(v[1]):
                if k != 'p1':
                    print(k, end=' ') 
        print('completed')
        break

def preemptivve(d):
    d = dict(sorted(d.items(), key=lambda x:x[1][0]))
    time = 0
    queue = list(d.keys()) 
    print("Queue : ", queue)
    burst_times = {process : d[process][1] for process in d}
    print('burst_time', burst_times)
    priority = {process : d[process][2] for process in d} 
    print('priority_order' ,priority) 
    remaining_burst_times = burst_times.copy()

    gantt_chart = [] 
    while queue:
        eligible_process = [process for process in queue if d[process][0] <= time]

        if len(eligible_process) > 1:
            h = max(eligible_process, key=lambda x:priority[x]) 
            time += remaining_burst_times[h]
            for i in range(remaining_burst_times[h] - 1):
                gantt_chart.append(h)
            remaining_burst_times[h] -= remaining_burst_times[h]
            gantt_chart.append(h)

            if remaining_burst_times[h] == 0: 
                queue.remove(h)
        elif not eligible_process: 
            time += 1
        else:
            higher_priority = min(eligible_process, key= lambda x: remaining_burst_times[x])
            time += 1
            remaining_burst_times[higher_priority] -= 1 
            gantt_chart.append(higher_priority)

            if remaining_burst_times[higher_priority] == 0: 
                queue.remove(higher_priority)
    print(gantt_chart)

d = {'A': [1, 5, 2], 'B': [3, 6, 1], 'C': [2, 7, 3]}
number_of_input = int(input("Enter the number of processes : ")) 
for i in range(number_of_input):
    process = input("Enter the process name :")
    arr = int(input(f"Enter the arrival time of {process}:"))
    bur = int(input(f"Enter the burst time of {process}:")) 
    priority = int(input(f"Enter the priority of {process}:")) 
    d[process] = [arr, bur, priority]
print('NON PREEMPTIVE')
nonpreemptive(d) 
print('PREEMPTIVE')
preemptivve(d)
