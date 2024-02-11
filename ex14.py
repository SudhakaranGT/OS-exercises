class Banker:
    def __init__(self, n_processes, n_resources, max_claim, allocation):
        self.n_processes = n_processes
        self.n_resources = n_resources
        self.max_claim = max_claim
        self.allocation = allocation
        self.need = [[max_claim[i][j] - allocation[i][j] for j in range(n_resources)] for i in range(n_processes)]
        self.available = [sum(max_claim[j][i] for j in range(n_processes)) - sum(allocation[j][i] for j in range(n_processes)) for i in range(n_resources)]
        self.safe_sequence = []

    def is_safe_state(self, process, work, finish):
        for i in range(self.n_resources):
            if self.need[process][i] > work[i]:
                return False
        return not finish[process]

    def safety_check(self):
        work = self.available.copy()
        finish = [False] * self.n_processes

        for _ in range(self.n_processes):
            found = False
            for i in range(self.n_processes):
                if not finish[i] and self.is_safe_state(i, work, finish):
                    for j in range(self.n_resources):
                        work[j] += self.allocation[i][j]
                    self.safe_sequence.append(i)
                    finish[i] = True
                    found = True
                    break

            if not found:
                return False

        return True

    def request_resources(self, process, request):
        for i in range(self.n_resources):
            if request[i] > self.need[process][i] or request[i] > self.available[i]:
                print(f"Error: Process {process} requesting more than needed or available resources.")
                return False

        for i in range(self.n_resources):
            self.available[i] -= request[i]
            self.allocation[process][i] += request[i]
            self.need[process][i] -= request[i]

        if not self.safety_check():
            # Rollback the changes if the state is not safe
            for i in range(self.n_resources):
                self.available[i] += request[i]
                self.allocation[process][i] -= request[i]
                self.need[process][i] += request[i]

            print("Request denied. System is not in a safe state.")
            return False

        print(f"Request granted. Safe sequence: {self.safe_sequence}")
        return True

# Example usage
if __name__ == "__main__":
    n_processes = 5
    n_resources = 3

    max_claim = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    allocation = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    banker = Banker(n_processes, n_resources, max_claim, allocation)

    # Example: Process 1 requests resources [0, 1, 0]
    banker.request_resources(1, [0, 3, 0])





NP = 5
NR = 4
allocation= []
max_claim = []
avail = []

need  = max_claim - allocation

for i in need:
     if need < avail:
          avail =  avail + allocation
     else:
         not_= [ ]