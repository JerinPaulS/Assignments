import collections
import math

PROCESS = collections.defaultdict(list)
PROCESS_COUNT = 3

def Data_Input():
    PROCESS = {"1": [3, 20], "2": [2, 5], "3": [2, 10]}
    execution_time = [20, 5, 10]
    '''
    PROCESS_COUNT = int(input("Enter the number of processes: "))
    for i in range(PROCESS_COUNT):
        ET = int(input("Enter the Execution Time of processes P" + str(i + 1) + ": "))
        TP = int(input("Enter the Time Period of processes P" + str(i + 1) + ": "))
        PROCESS[i + 1] = [ET, TP]
        execution_time.append(TP)
    '''

    total = 0
    for p in PROCESS:
        total += (PROCESS_COUNT * ((2 ** (1 / PROCESS_COUNT)) - 1))

    if total >= 1:
        print("CPU Over Utilization Error!!", total)
        return
    total_time = math.lcm(execution_time)

Data_Input()