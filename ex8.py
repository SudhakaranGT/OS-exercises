def round_robin_scheduler(processes, time_quantum):
    queue = list(processes.keys())
    gantt_chart = []
    current_time = 0

    while queue:
        for process in queue.copy():
            if processes[process][0] <= current_time:
                execute_time = min(processes[process][1], time_quantum)
                for _ in range(execute_time):
                    gantt_chart.append(process)
                processes[process][1] -= execute_time
                current_time += execute_time

                if processes[process][1] == 0:
                    queue.remove(process)
                else:
                    queue.append(queue.pop(0))

    return gantt_chart

if __name__ == "__main__":
    processes = {'p1': [0, 5], 'p2': [1, 6], 'p3': [2, 3], 'p4': [3, 1], 'p5': [4, 5], 'p6': [6, 4]}
    time_quantum = 4
    gantt_chart = round_robin_scheduler(processes, time_quantum)
    print("Gantt Chart:")
    print(gantt_chart)
