import math
import random
import matplotlib.pyplot as plt

def generate_first_solution(POP_SIZE, number):
    data = []
    if number == 1:
        for iter in range(POP_SIZE):
            temp = []
            for col in range(10):
                temp.append(random.randint(-35, 35))
            data.append(temp)
        return data
    elif number == 2:
        for iter in range(POP_SIZE):
            temp = []
            for col in range(10):
                temp.append(random.randint(-100, 100))
            data.append(temp)
        return data
    else:
        for iter in range(POP_SIZE):
            temp = []
            for col in range(10):
                temp.append(random.randint(-200, 200))
            data.append(temp)
        return data

def evaluation(row, number):
    if number == 1:
        return benchmarkFunc1(row)
    elif number == 2:
        return benchmarkFunc2(row)
    elif number == 3:
        return benchmarkFunc3(row)
    elif number == 4:
        return benchmarkFunc4(row)
    elif number == 5:
        return benchmarkFunc5(row)

def fitness(row, number):
    result = evaluation(row, number)
    '''
    if result == 0:
        return 10 ** 6
    else:
        return (1 / result)
    '''
    return result - 0

def reproduce(data, pc):
    temp_data = data.copy()
    new_data = data.copy()
    while len(temp_data) > 2:
        p1 = temp_data.pop(random.randint(0, len(temp_data) - 1))
        p2 = temp_data.pop(random.randint(0, len(temp_data) - 1))
        r = random.uniform(0, 1)
        if r < pc:
            # 0   1   2   3   4   5   6   7   8   9
            # 0   1   2   3   4   5   6   7   8   9
            c1, c2 = p1[:100] + p2[100:200] + p1[200:600] + p2[600:800] + p1[800:], p2[:100] + p1[100:200] + p2[200:600] + p1[600:800] + p2[800:]
            new_data.append(c1)
            new_data.append(c2)
    return new_data

def variate(number, data, pm):
    for index, row in enumerate(data):
        r = random.uniform(0, 1)
        if r > pm:
            pos1, pos2 = random.randint(0, 9), random.randint(0, 9)
            #pos3, pos4 = random.randint(0, 9), random.randint(0, 9)

            if number == 1:
                data[index][pos1], data[index][pos2] = random.randint(-35, 35), random.randint(-35, 35)
                #data[index][pos3], data[index][pos4] = random.randint(-35, 35), random.randint(-35, 35)
            elif number == 2:
                data[index][pos1], data[index][pos2] = random.randint(-100, 100), random.randint(-100, 100)
                #data[index][pos3], data[index][pos4] = random.randint(-100, 100), random.randint(-100, 100)
            else:
                data[index][pos1], data[index][pos2] = random.randint(-200, 200), random.randint(-200, 200)
                #data[index][pos3], data[index][pos4] = random.randint(-200, 200), random.randint(-200, 200)
    return data

def select_pop(data, fit, POP_SIZE):
    total = []
    for index, row in enumerate(data):
        temp = []
        temp.append(row)
        temp.append(fit[index])
        total.append(temp)
    #print(total)
    sorted_total = sorted(total, key = lambda x: x[1])
    new_pop = []
    count = 0
    fit = []
    #print(POP_SIZE)
    for index in range(len(sorted_total)):
        if count == POP_SIZE:
            break
        count += 1
        new_pop.append(sorted_total[index][0])
        fit.append(sorted_total[index][1])
    temp = []
    temp.append(new_pop)
    temp.append(fit)
    return temp

def benchmarkFunc1(row):
    #Ackley 1 Function
    #print(row)
    firstSum = 0.0
    secondSum = 0.0
    for c in row:
        firstSum += c ** 2.0
        secondSum += math.cos(2.0 * math.pi * c)
    n = float(len(row))
    return -20.0 * math.exp(-0.2 * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + 20 + math.e

def benchmarkFunc2(row):
    #Chung Reynolds Function
    firstSum = 0.0
    for c in row:
        firstSum += c ** 2.0
    return firstSum ** 2

def benchmarkFunc3(row):
    #Schumer Steiglitz Function
    firstSum = 0.0
    for c in row:
        firstSum += c ** 4
    return firstSum

def benchmarkFunc4(row):
    #Zigzag Function
    firstSum = 0.0
    for c in row:
        lamb = random.uniform(0, 1)
        #k = random.randint(1, 16)
        k = 16
        m = random.randint(0, 1)
        val = (abs(c) / k) - math.floor((abs(c) / k))
        z = 0
        if val <= lamb:
            z = 1 - m + (m / lamb * val)
        else:
            z = 1 - m + (m / (1 - lamb) * val)

        firstSum += 3 * 10 ** 9 * abs((c - 40) * (c - 185) * c * (c + 50) * (c + 180)) * z + (10 * math.sin(0.1 * c))
    return firstSum

def benchmarkFunc5(row):
    #SSchwefel 2.22 Function
    firstSum = 0.0
    secondSum = 0.0
    for c in row:
        firstSum += abs(c)
        secondSum *= abs(c)
    return firstSum + secondSum

def genetic_algo():
    POP_SIZE = 1000
    data1 = generate_first_solution(POP_SIZE, 1)
    data2 = generate_first_solution(POP_SIZE, 2)
    data3 = data2.copy()
    data4 = generate_first_solution(POP_SIZE, 3)
    data5 = data1.copy()
    ITERATIONS = 500
    Functions = {1: "Ackley 1 Function", 2: "Chung Reynolds Function", 3: "Schumer Steiglitz Function", 4: "Zigzag Function", 5: "SSchwefel 2.22 Function"}
    X = list(range(0, ITERATIONS))
    Y = []
    for i in range(1):
        fit = []
        if i == 0:
            data = data1
        elif i == 1:
            data = data2
        elif i == 2:
            data = data3
        elif i == 3:
            data = data4
        elif i == 4:
            data = data5
        for row in data:
            fit.append(fitness(row, i + 1))
        best_fit = float("inf")
        print(data[0], best_fit)
        print("\n")
        temp_axis = []
        for iterations in range(ITERATIONS):
            #print(data)
            tt = data.copy()
            print("\t\t***** " + Functions[i + 1] + " Iteration Number " + str(iterations) + " *****")
            new_population = reproduce(data, 0.9)
            #print(new_population)
            new_population = variate(i + 1, new_population, 0.1)
            #print(new_population)
            fit = []
            for row in new_population:
                fit.append(fitness(row, i + 1))
            temp = select_pop(new_population, fit, POP_SIZE)
            data = []
            data, fit = temp[0], temp[1]
            #print("is data same " + str(data == tt))
            print(data[0], best_fit)
            if fit[0] < best_fit:
                best_fit = fit[0]
            print("\n")
            if i == 0:
                temp_axis.append(best_fit)
            elif i == 1:
                temp_axis.append(best_fit)
            elif i == 2:
                temp_axis.append(best_fit)
            elif i == 3:
                temp_axis.append(best_fit)
            elif i == 4:
                temp_axis.append(best_fit)
        Y.append(temp_axis)
    #print(data[0], 1/fit[0])
    #print(Y)
    figure, axis = plt.subplots(3, 2)
    axis[0, 0].plot(X, Y[0])
    axis[0, 0].set_title("Ackley 1 Function")
    '''
    axis[0, 1].plot(X, Y[1])
    axis[0, 1].set_title("Chung Reynolds Function")
    axis[1, 0].plot(X, Y[2])
    axis[1, 0].set_title("Schumer Steiglitz Function")
    axis[1, 1].plot(X, Y[3])
    axis[1, 1].set_title("Zigzag Function")
    axis[2, 0].plot(X, Y[4])
    axis[2, 0].set_title("SSchwefel 2.22 Function")
    '''
    plt.show()
    return

genetic_algo()
