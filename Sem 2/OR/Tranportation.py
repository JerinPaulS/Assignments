class Transport:
    def __init__(self):
        '''
        GRID = [[3, 1, 7, 4], [2, 6, 5, 9], [8, 3, 3, 2]]
        SUPPLY = [300, 400, 500]
        DEMAND = [250, 350, 400, 200]
        ROWS = 3
        COLS = 4
        '''
        self.GRID = []
        self.SUPPLY = []
        self.DEMAND = []
        self.ROWS = 0
        self.COLS = 0
        self.ALLOCATION = []

    def display(self, val, lst):
        print("\n" + val)
        for row in lst:
            print(row)

    def calcCost(self):
        total = 0
        for row in range(self.ROWS):
            for col in range(self.COLS):
                total += (self.ALLOCATION[row][col] * self.GRID[row][col])

        print("The cost of the problem is = " + str(total))

    def createTable(self):
        print("\nTaking the input for the cost matrix\n")
        self.ROWS = int(input("Enter the number of sources: "))
        self.COLS = int(input("Enter the number of destinations: "))
        for row in range(self.ROWS):
            temp = []
            for col in range(self.COLS):
                cost = int(input("Enter the cost of transportation from S" + str(row + 1) + " to D" + str(col + 1) + ": "))
                temp.append(cost)
            self.GRID.append(temp)
        print("\n\nTaking the input for the demand\n")
        for col in range(self.COLS):
            demand = int(input("Enter the demand for D" + str(col + 1) + ": "))
            self.DEMAND.append(demand)
        print("\n\nTaking the input for the supply\n")
        for row in range(self.ROWS):
            supply = int(input("Enter the supply for S" + str(row + 1) + ": "))
            self.SUPPLY.append(supply)

    def leastCost(self):
        self.ALLOCATION = []
        for row in range(self.ROWS):
            temp = []
            for col in range(self.COLS):
                temp.append(0)
            self.ALLOCATION.append(temp)

        temp_supply, temp_demand = self.SUPPLY.copy(), self.DEMAND.copy()
        min_row, min_col, min_cost = -1, -1, 10 ** 10
        while sum(temp_demand) > 0 and sum(temp_supply) > 0:
            for row in range(self.ROWS):
                for col in range(self.COLS):
                    if self.GRID[row][col] < min_cost and temp_supply[row] > 0 and temp_demand[col] > 0:
                        min_cost = self.GRID[row][col]
                        min_row = row
                        min_col = col
            alloc = min(temp_supply[min_row], temp_demand[min_col])
            temp_supply[min_row] -= alloc
            temp_demand[min_col] -= alloc
            self.ALLOCATION[min_row][min_col] = alloc
            min_row, min_col, min_cost = -1, -1, 10 ** 10

        self.display("ALLOCATIONS", self.ALLOCATION)
        self.calcCost()

    def NWmethod(self):
        self.ALLOCATION = []
        for row in range(self.ROWS):
            temp = []
            for col in range(self.COLS):
                temp.append(0)
            self.ALLOCATION.append(temp)

        temp_supply, temp_demand = self.SUPPLY.copy(), self.DEMAND.copy()
        row, col = 0, 0
        while sum(temp_demand) > 0 and sum(temp_supply) > 0:
            if 0 <= row < self.ROWS and 0 <= col < self.COLS:
                if temp_supply[row] < temp_demand[col]:
                    alloc = temp_supply[row]
                    self.ALLOCATION[row][col] = alloc
                    temp_supply[row] -= alloc
                    temp_demand[col] -= alloc
                    row += 1
                else:
                    alloc = temp_demand[col]
                    self.ALLOCATION[row][col] = alloc
                    temp_supply[row] -= alloc
                    temp_demand[col] -= alloc
                    col += 1
            else:
                break

        self.display("ALLOCATIONS", self.ALLOCATION)
        self.calcCost()

obj = Transport()
obj.createTable()
obj.leastCost()
obj.NWmethod()
