GRID = [[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]]
SUPPLY = [300, 400, 500]
DEMAND = [250, 350, 400, 200]
ROWS = 3
COLS = 4
ALLOCATION = []

def display(val, lst):
    print("\n" + val)
    for row in lst:
        print(row)

def calcCost():
    total = 0
    for row in range(ROWS):
        for col in range(COLS):
            total += (ALLOCATION[row][col] * GRID[row][col])
    
    print("The cost of the problem is = " + str(total))

def createTable():
    print("\nTaking the input for the cost matrix\n")
    ROWS = int(input("Enter the number of sources: "))
    COLS = int(input("Enter the number of destinations: "))
    for row in range(ROWS):
        temp = []
        for col in range(COLS):
            cost = int(input("Enter the cost of transportation from S" + str(row + 1) + " to D" + str(col + 1) + ": "))
            temp.append(cost)
        GRID.append(temp)
    print("\n\nTaking the input for the demand\n")
    for col in range(COLS):
        demand = int(input("Enter the demand for D" + str(col + 1) + ": "))
        DEMAND.append(demand)
    print("\n\nTaking the input for the supply\n")
    for row in range(ROWS):
        supply = int(input("Enter the supply for S" + str(row + 1) + ": "))
        SUPPLY.append(supply)

def leastCost():
    for row in range(ROWS):
        temp = []
        for col in range(COLS):
            temp.append(0)
        ALLOCATION.append(temp)

    temp_supply, temp_demand = SUPPLY.copy(), DEMAND.copy()
    min_row, min_col, min_cost = -1, -1, 10 ** 10
    while sum(temp_demand) > 0 and sum(temp_supply) > 0:
        for row in range(ROWS):
            for col in range(COLS):
                if GRID[row][col] < min_cost and temp_supply[row] > 0 and temp_demand[col] > 0:
                    min_cost = GRID[row][col]
                    min_row = row
                    min_col = col
        alloc = min(temp_supply[min_row], temp_demand[min_col])     
        temp_supply[min_row] -= alloc
        temp_demand[min_col] -= alloc
        ALLOCATION[min_row][min_col] = alloc
        min_row, min_col, min_cost = -1, -1, 10 ** 10

    display("ALLOCATIONS", ALLOCATION)
    calcCost()

def NWmethod():
    for row in range(ROWS):
        temp = []
        for col in range(COLS):
            temp.append(0)
        ALLOCATION.append(temp)

    temp_supply, temp_demand = SUPPLY.copy(), DEMAND.copy()
    row, col = 0, 0
    while sum(temp_demand) > 0 and sum(temp_supply) > 0:
        if temp_supply[row] < temp_demand[col]:
            alloc = temp_supply[row]
            ALLOCATION[row][col] = alloc
            row += 1
        else:
            alloc = temp_demand[col]
            ALLOCATION[row][col] = alloc
            col += 1
        if 0 <= row < ROWS and 0 <= col < COLS:
            temp_supply[row] -= alloc
            temp_demand[col] -= alloc            
        else:
            break

    display("ALLOCATIONS", ALLOCATION)
    calcCost()

#createTable()
#leastCost()
NWmethod()