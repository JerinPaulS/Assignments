import collections
class JobScheduling:
    def __init__(self):
        self.jobs = 0
        self.bt = []
        self.at = []
        self.qunatum = 0
        self.algo = 0
        self.current_time = 0
        #{PID: AT BT CT TAT WT}
        #TAT = CT - AT
        #WT = TAT - BT
        self.data = collections.defaultdict(list)

    def interact(self):
        self.jobs = int(input("\t\tEnter the number of jobs: "))
        self.at = list(map(int, input("\t\tEnter AT of jobs (Space Separated): ").split()))
        self.current_time = min(self.at)
        self.bt = list(map(int, input("\t\tEnter BT of jobs (Space Separated): ").split()))
        temp = 0

        while temp < self.jobs:
            self.data[temp + 1].append(self.at[temp])
            self.data[temp + 1].append(self.bt[temp])
            temp += 1

        while True:
            print("\t\tSelect the Scheduler Type:\n\t\t 1. Shortest Job First\n\t\t 2. First Come First Serve\n\t\t 3. Round Robin")
            self.algo = int(input("\t\tYour choice is: "))
            if self.algo != 1 and self.algo != 2 and self.algo != 3:
                continue
            else:
                break
        if self.algo == 1:
            self.SJF()
        elif self.algo == 2:
            self.FCFS()
        elif self.algo == 3:
            self.qunatum = int(input("\t\tEnter the quantum time: "))
            self.RR()

        self.display()

        choice = input("\t\tDo you wish to continue? ")
        positive = ["YES", "Yes", "yes", "y", "Y"]
        if choice in positive:
            self.data = collections.defaultdict(list)
            self.interact()
        else:
            return

    def display(self):
        self.data = sorted(self.data, key = lambda x: x[0])
        print("\n\t\tPID\tAT\tBT\tCT\tTAT\tWT")
        for d in self.data:
            d[1].append(d[1][2] - d[1][0])
            d[1].append(d[1][3] - d[1][1])
            d[1].append(d[1][4] - d[1][2])
            print("\t", str(d[0]), str(d[1][0]), str(d[1][1]), str(d[1][2]), str(d[1][3]), str(d[1][4]), sep = " \t")
        return

    def SJF(self):
        self.data = sorted(self.data.items(), key = lambda x: (x[1][1], x[1][0]))
        for d in self.data:
            while d[1][0] > self.current_time:
                self.current_time += 1
            self.current_time += d[1][1]
            d[1].append(self.current_time)
        return

    def FCFS(self):
        self.data = sorted(self.data.items(), key = lambda x: (x[1][0], x[0]))
        print(self.data)
        for d in self.data:
            while d[1][0] > self.current_time:
                self.current_time += 1
            self.current_time += d[1][1]
            d[1].append(self.current_time)
        return

    def RR(self):

        return


obj = JobScheduling()
obj.interact()
