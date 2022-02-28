import random
import collections

board = []
N = 8
POP_SIZE = 100
ITERATIONS = 100

def generate_population(POP_SIZE):
    DATA = []
    occupied = set()
    for pop in range(POP_SIZE):
        count = 0
        temp = []
        while count < N:
            if len(occupied) == N * N:
                break
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if (row, col) not in occupied:
                count += 1
                occupied.add((row, col))
                temp.append((row, col))
        occupied.clear()
        DATA.append(temp)
    return DATA

def display(positions):
    board = []
    for row in range(N):
        temp = []
        for col in range(N):
            if (row, col) in positions:
                temp.append("Q")
                print(" Q ", end = "")
            else:
                temp.append(" ")
                print(" . ", end = "")
        board.append(temp)
        print()

def evaluation_func(curr_pop, row, col):
    return rowScore(curr_pop, row, col) + colScore(curr_pop, row, col) + diagScore(curr_pop, row, col)

def fitness(curr_pop, row, col):
    return evaluation_func(curr_pop, row, col) - 0

def rowScore(curr_pop, row, col):
    rows = 0
    for c in range(N):
        if col == c:
            continue
        if (row, c) in curr_pop:
            rows += 1
    #print(curr_pop, rows)
    return rows

def colScore(curr_pop, row, col):
    cols = 0
    for r in range(N):
        if row == r:
            continue
        if (r, col) in curr_pop:
            cols += 1
    #print(curr_pop, cols)
    return cols

def diagScore(curr_pop, row, col):
    posDiag, posDiag1 = 0, 0
    negDiag, negDiag1 = 0, 0
    r, c = row + 1, col + 1
    while 0 <= r < N and 0 <= c < N:
        if (r, c) in curr_pop:
            posDiag += 1
        r += 1
        c += 1
    r, c = row - 1, col - 1
    while 0 <= r < N and 0 <= c < N:
        if (r, c) in curr_pop:
            negDiag += 1
        r -= 1
        c -= 1
    r, c = row - 1, col + 1
    while 0 <= r < N and 0 <= c < N:
        if (r, c) in curr_pop:
            posDiag1 += 1
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while 0 <= r < N and 0 <= c < N:
        if (r, c) in curr_pop:
            negDiag1 += 1
        r += 1
        c -= 1
    #print(curr_pop, posDiag + negDiag)
    return posDiag + negDiag + posDiag1 + negDiag1

def direction(curr_pop, row, col):
    directions = [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
    for d in directions:
        new_x, new_y = d[0] + row, d[1] + col
        if 0 <= new_x < N and 0 <= new_y < N:
            if (new_x, new_y) not in curr_pop:
                return (new_x, new_y)
    return (-1, -1)

def select_population(population):
    population.sort(key = lambda x:x[1])
    data = population[:80]
    #print(data, len(data))
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i][0])
    new_data += generate_population(20)
    #print(new_data, len(new_data))
    return new_data

def PSO():
    r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
    w, c1, c2 = 2, 2, 2
    pbest, gbest = 10 ** 5, 10 ** 5
    new_x, new_y = 0, 0
    vx, vy = 1, 1
    DATA = generate_population(100)
    for i in range(ITERATIONS):
        population = []
        print("\n\t *** ITERATION " + str(i + 1) + "***")
        for p in DATA:
            temp = []
            total = 0
            for index, individual in enumerate(p):
                row, col = individual
                #print(row, col, p, fitness(p, row, col))
                #display(p)
                total += fitness(p, row, col)
                #print("PBEST", pbest)
                x, y = direction(p, row, col)
                vx = (w * vx) + (c1 * r1 * (pbest - x)) + (c1 * r1 * (gbest - x))
                vy = (w * vy) + (c1 * r1 * (pbest - y)) + (c1 * r1 * (gbest - y))
                if 0 <= row + vx < N and 0 <= col + vy < N and (row + vx, col + vy) not in p:
                    new_x = row + vx
                    new_y = col + vy
                    p[index] = (new_x, new_y)
            #print(pbest, gbest)
            #return
            pbest = min(pbest, total)
            temp.append(p)
            temp.append(pbest)
            population.append(temp)
        gbest = min(gbest, pbest)
        print("\t\tGBest " + str(gbest))
        DATA = select_population(population)
    display(DATA[0])
    total = 0
    for p in DATA[0]:
        total += fitness(DATA[0], p[0], p[1])
    print(total)
    return

PSO()
