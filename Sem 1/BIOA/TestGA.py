import math
import random
import matplotlib.pyplot as plt

teams = ["Arsenal", "Aston Villa", "Blackburn", "Chelsea", "Everton", "Liverpool", "Machester Utd", "Manchester City", "Southampton", "Tottenham"]

TEAMS = {"Arsenal": ["Emirates Stadium", "London", "Hilton"],
            "Aston Villa": ["Villa Park", "Aston", "Holiday Inn"],
            "Blackburn": ["Ewood Park", "Leamington", "Blackburn Hotel"],
            "Chelsea": ["Stamford Bridge", "Fulham", "Millennium & Copthorne"],
            "Everton": ["Goodison Park", "Walton", "Dixie Dean"],
            "Liverpool": ["Anfield", "Merseyside", "Hope Street"],
            "Machester Utd": ["Old Trafford", "Old Trafford", "Hyatt"],
            "Manchester City": ["Etihad Stadium", "East Manchester", "Emirates Palace"],
            "Southampton": ["St Mary's", "Southampton", "Jury's Inn"],
            "Tottenham": ["Tottenham Hotspur", "North London", "Myddelton Lodge"]}
HOTELS = {"Arsenal": [5250, "London", "Hilton"],
            "Aston Villa": [5435, "Aston", "Holiday Inn"],
            "Blackburn": [5676, "Leamington", "Blackburn Hotel"],
            "Chelsea": [5800, "Fulham", "Millennium & Copthorne"],
            "Everton": [5500, "Walton", "Dixie Dean"],
            "Liverpool": [5570, "Merseyside", "Hope Street"],
            "Machester Utd": [5000, "Old Trafford", "Hyatt"],
            "Manchester City": [5565, "East Manchester", "Emirates Palace"],
            "Southampton": [5510, "Southampton", "Jury's Inn"],
            "Tottenham": [5005, "North London", "Myddelton Lodge"]}
STADIUMS = {"Emirates Stadium": ["London", 55260],
                "Villa Park": ["Aston",52785],
                "Ewood Park": ["Leamington",53367],
                "Stamford Bridge": ["Fulham",54837],
                "Goodison Park": ["Walton",59572],
                "Anfield": ["Merseyside",53394],
                "Old Trafford": ["Old Trafford",58000],
                "Etihad Stadium": ["East Manchester",55097],
                "St Mary's": ["Southampton",52505],
                "Tottenham Hotspur": ["North London",56850]}
ROUTES = {("London", "Aston"): 12200,
            ("London", "Leamington"): 18100,
            ("London", "Walton"): 11500,
            ("London", "Fulham"): 13600,
            ("London", "Merseyside"): 12180,
            ("London", "Old Trafford"): 19990,
            ("London", "East Manchester"): 11120,
            ("London", "Southampton"): 18000,
            ("London", "North London"): 11400,
            ("Aston", "Leamington"): 13720,
            ("Aston", "Fulham"): 10100,
            ("Aston", "Walton"): 13190,
            ("Aston", "Merseyside"): 19620,
            ("Aston", "Old Trafford"): 18580,
            ("Aston", "East Manchester"): 12240,
            ("Aston", "Southampton"): 14360,
            ("Aston", "North London"): 11820,
            ("Leamington", "Fulham"): 11180,
            ("Leamington", "Walton"): 12400,
            ("Leamington", "Merseyside"): 12980,
            ("Leamington", "Old Trafford"): 11920,
            ("Leamington", "East Manchester"): 11970,
            ("Leamington", "Southampton"): 11260,
            ("Leamington", "North London"): 11220,
            ("Fulham", "Walton"): 11700,
            ("Fulham", "Merseyside"): 17707,
            ("Fulham", "Old Trafford"): 17800,
            ("Fulham", "East Manchester"): 18840,
            ("Fulham", "Southampton"): 16400,
            ("Fulham", "North London"): 14000,
            ("Walton", "Merseyside"): 15600,
            ("Walton", "Old Trafford"): 11400,
            ("Walton", "East Manchester"): 19780,
            ("Walton", "Southampton"): 14510,
            ("Walton", "North London"): 11340,
            ("Merseyside", "Old Trafford"): 13090,
            ("Merseyside", "East Manchester"): 15430,
            ("Merseyside", "Southampton"): 13610,
            ("Merseyside", "North London"): 12140,
            ("Old Trafford", "East Manchester"): 11310,
            ("Old Trafford", "Southampton"): 12510,
            ("Old Trafford", "North London"): 11080,
            ("East Manchester", "Southampton"): 12540,
            ("East Manchester", "North London"): 11120,
            ("Southampton", "North London"): 18270}
T_BM1 = {"Arsenal": random.randint(-35, 35), "Aston Villa": random.randint(-35, 35), "Blackburn": random.randint(-35, 35), "Chelsea": random.randint(-35, 35), "Everton": random.randint(-35, 35), "Liverpool": random.randint(-35, 35), "Machester Utd": random.randint(-35, 35), "Manchester City": random.randint(-35, 35), "Southampton": random.randint(-35, 35), "Tottenham": random.randint(-35, 35)}
H_BM1 = {"Hilton": random.randint(-35, 35), "Holiday Inn": random.randint(-35, 35),"Blackburn Hotel": random.randint(-35, 35), "Millennium & Copthorne":random.randint(-35, 35), "Dixie Dean": random.randint(-35, 35), "Hope Street": random.randint(-35, 35), "Hyatt": random.randint(-35, 35), "Emirates Palace": random.randint(-35, 35), "Jury's Inn": random.randint(-35, 35), "Myddelton Lodge": random.randint(-35, 35)}
D_BM1 = {"Sunday": random.randint(-35, 35), "Monday": random.randint(-35, 35), "Tuesday": random.randint(-35, 35), "Wednesday": random.randint(-35, 35), "Thursday": random.randint(-35, 35), "Friday": random.randint(-35, 35), "Saturday": random.randint(-35, 35)}
C_BM1 = {"London": random.randint(-35, 35), "Aston": random.randint(-35, 35), "Leamington": random.randint(-35, 35), "Fulham": random.randint(-35, 35), "Walton": random.randint(-35, 35), "Merseyside": random.randint(-35, 35), "Old Trafford": random.randint(-35, 35), "East Manchester": random.randint(-35, 35), "Southampton": random.randint(-35, 35), "North London": random.randint(-35, 35)}
S_BM1 = {"Emirates Stadium": random.randint(-35, 35), "Villa Park": random.randint(-35, 35), "Ewood Park": random.randint(-35, 35), "Stamford Bridge": random.randint(-35, 35), "Goodison Park": random.randint(-35, 35), "Anfield": random.randint(-35, 35), "Old Trafford": random.randint(-35, 35), "Etihad Stadium": random.randint(-35, 35), "St Mary's": random.randint(-35, 35), "Tottenham Hotspur": random.randint(-35, 35)}

T_BM2 = {"Arsenal": random.randint(-100, 100), "Aston Villa": random.randint(-100, 100), "Blackburn": random.randint(-100, 100), "Chelsea": random.randint(-100, 100), "Everton": random.randint(-100, 100), "Liverpool": random.randint(-100, 100), "Machester Utd": random.randint(-100, 100), "Manchester City": random.randint(-100, 100), "Southampton": random.randint(-100, 100), "Tottenham": random.randint(-100, 100)}
H_BM2 = {"Hilton": random.randint(-100, 100), "Holiday Inn": random.randint(-100, 100),"Blackburn Hotel": random.randint(-100, 100), "Millennium & Copthorne": random.randint(-100, 100), "Dixie Dean": random.randint(-100, 100), "Hope Street": random.randint(-100, 100), "Hyatt": random.randint(-100, 100), "Emirates Palace": random.randint(-100, 100), "Jury's Inn": random.randint(-100, 100), "Myddelton Lodge": random.randint(-100, 100)}
D_BM2 = {"Sunday": random.randint(-100, 100), "Monday": random.randint(-100, 100), "Tuesday": random.randint(-100, 100), "Wednesday": random.randint(-100, 100), "Thursday": random.randint(-100, 100), "Friday": random.randint(-100, 100), "Saturday": random.randint(-100, 100)}
C_BM2 = {"London": random.randint(-100, 100), "Aston": random.randint(-100, 100), "Leamington": random.randint(-100, 100), "Fulham": random.randint(-100, 100), "Walton": random.randint(-100, 100), "Merseyside": random.randint(-100, 100), "Old Trafford": random.randint(-100, 100), "East Manchester": random.randint(-100, 100), "Southampton": random.randint(-100, 100), "North London": random.randint(-100, 100)}
S_BM2 = {"Emirates Stadium": random.randint(-100, 100), "Villa Park": random.randint(-100, 100), "Ewood Park": random.randint(-100, 100), "Stamford Bridge": random.randint(-100, 100), "Goodison Park": random.randint(-100, 100), "Anfield": random.randint(-100, 100), "Old Trafford": random.randint(-100, 100), "Etihad Stadium": random.randint(-100, 100), "St Mary's": random.randint(-100, 100), "Tottenham Hotspur": random.randint(-100, 100)}

T_BM3 = {"Arsenal": random.randint(-200, 200), "Aston Villa": random.randint(-200, 200), "Blackburn": random.randint(-200, 200), "Chelsea": random.randint(-200, 200), "Everton": random.randint(-200, 200), "Liverpool": random.randint(-200, 200), "Machester Utd": random.randint(-200, 200), "Manchester City": random.randint(-200, 200), "Southampton": random.randint(-200, 200), "Tottenham": random.randint(-200, 200)}
H_BM3 = {"Hilton": random.randint(-200, 200), "Holiday Inn": random.randint(-200, 200),"Blackburn Hotel": random.randint(-200, 200), "Millennium & Copthorne": random.randint(-200, 200), "Dixie Dean": random.randint(-200, 200), "Hope Street": random.randint(-200, 200), "Hyatt": random.randint(-200, 200), "Emirates Palace": random.randint(-200, 200), "Jury's Inn": random.randint(-200, 200), "Myddelton Lodge": random.randint(-200, 200)}
D_BM3 = {"Sunday": random.randint(-200, 200), "Monday": random.randint(-200, 200), "Tuesday": random.randint(-200, 200), "Wednesday": random.randint(-200, 200), "Thursday": random.randint(-200, 200), "Friday": random.randint(-200, 200), "Saturday": random.randint(-200, 200)}
C_BM3 = {"London": random.randint(-200, 200), "Aston": random.randint(-200, 200), "Leamington": random.randint(-200, 200), "Fulham": random.randint(-200, 200), "Walton": random.randint(-200, 200), "Merseyside": random.randint(-200, 200), "Old Trafford": random.randint(-200, 200), "East Manchester": random.randint(-200, 200), "Southampton": random.randint(-200, 200), "North London": random.randint(-200, 200)}
S_BM3 = {"Emirates Stadium": random.randint(-200, 200), "Villa Park": random.randint(-200, 200), "Ewood Park": random.randint(-200, 200), "Stamford Bridge": random.randint(-200, 200), "Goodison Park": random.randint(-200, 200), "Anfield": random.randint(-200, 200), "Old Trafford": random.randint(-200, 200), "Etihad Stadium": random.randint(-200, 200), "St Mary's": random.randint(-200, 200), "Tottenham Hotspur": random.randint(-200, 200)}


def generate_first_solution():
    total = []
    #match = team1, team2, stadium, city, day
    t = {"Arsenal": 0, "Aston Villa": 0, "Blackburn": 0, "Chelsea": 0, "Everton": 0, "Liverpool": 0, "Machester Utd": 0, "Manchester City": 0, "Southampton": 0, "Tottenham": 0}
    h = {"Hilton": 0, "Holiday Inn": 0,"Blackburn Hotel": 0, "Millennium & Copthorne": 0, "Dixie Dean": 0, "Hope Street": 0, "Hyatt": 0, "Emirates Palace": 0, "Jury's Inn": 0, "Myddelton Lodge": 0}
    d = {"Sunday": 0, "Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0}
    c = {"London": 0, "Aston": 0, "Leamington": 0, "Fulham": 0, "Walton": 0, "Merseyside": 0, "Old Trafford": 0, "East Manchester": 0, "Southampton": 0, "North London": 0}
    s = {"Emirates Stadium": 0, "Villa Park": 0, "Ewood Park": 0, "Stamford Bridge": 0, "Goodison Park": 0, "Anfield": 0, "Old Trafford": 0, "Etihad Stadium": 0, "St Mary's": 0, "Tottenham Hotspur": 0}

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for team1 in teams:
        for team2 in teams:
            temp = []
            temp.append(team1)
            if team1 == team2:
                continue
            temp.append(team2)
            stadiums = [TEAMS[team1][0], TEAMS[team2][0]]
            std_choice = random.choice(stadiums)
            temp.append(std_choice)
            temp.append(STADIUMS[std_choice][0])
            temp.append(random.choice(days))
            total.append(temp)

    data = []
    for row in total:
        if t[row[0]] == 0 or t[row[1]] == 0 or s[row[2]] == 0 or c[row[3]] == 0 or d[row[4]] == 0:
            data.append(row)
            t[row[0]] = 1
            t[row[1]] = 1
            s[row[2]] = 1
            c[row[3]] = 1
            d[row[4]] = 1
    print(len(data))
    for row in data:
        total.remove(row)
    indices = random.sample(range(0, len(total)), 10)
    for index in indices:
        data.append(total[index])
    POP_SIZE = len(data)
    #print(data)
    return(data, POP_SIZE)

def evaluation(row):
    day_turnaround = {"Sunday": 0.98, "Monday": 0.55, "Tuesday": 0.65, "Wednesday": 0.75, "Thursday": 0.85, "Friday": 0.9, "Saturday": 0.95}
    hotel_exp = 0
    travel_exp = 0
    ticket_revenue = STADIUMS[row[2]][1] * day_turnaround[row[-1]]
    if TEAMS[row[0]][1] != row[3]:
        travel_exp = ROUTES.get((TEAMS[row[0]][1], row[3]), 0)
        travel_exp = ROUTES.get((row[3], TEAMS[row[0]][1]), 0)
        hotel_exp = HOTELS[row[1]][0]
    if TEAMS[row[1]][1] != row[3]:
        travel_exp += ROUTES.get((TEAMS[row[1]][1], row[3]), 0)
        travel_exp += ROUTES.get((row[3], TEAMS[row[1]][1]), 0)
        hotel_exp += HOTELS[row[0]][0]
    return ticket_revenue * 10 - travel_exp - hotel_exp

def fitness(row):
    data = result = evaluation(row)
    if row == 0:
        return 10 ** 6
    else:
        return (1 / result)

def reproduce(data, pc):
    temp_data = data.copy()
    new_data = data.copy()
    #print(temp_data)
    while len(temp_data) > 2:
        p1 = temp_data.pop(random.randint(0, len(temp_data) - 1))
        p2 = temp_data.pop(random.randint(0, len(temp_data) - 1))
        r = random.uniform(0, 1)
        if p1[0] == p2[1] or p1[1] == p2[0]:
            continue
        if r < pc:
            c1, c2 = p1.copy(), p2.copy()
            #Ateam1   Ateam2      Astaduim     ACity    Aday
            #Bteam1   Bteam2      Bstaduim     BCity    Bday
            choice = random.randint(1, 3)
            if choice == 1 and TEAMS[p1[1]][0] == p1[2] and TEAMS[p2[1]][0] == p2[2]:
                c1 = p1[:1] + p2[1:]
                c2 = p2[:1] + p1[1:]
            elif choice == 2:
                c1 = p1[:4] + p2[4:]
                c2 = p2[:4] + p1[4:]
            elif choice == 3 and TEAMS[p1[1]][0] == p1[2] and TEAMS[p2[1]][0] == p2[2]:
                c1 = p2[:1] + p1[1:]
                c2 = p1[:1] + p2[1:]
            #print(c1, c2)
            new_data.append(c1)
            new_data.append(c2)
    return new_data

def variate(data, pm):
    #match = team1, team2, stadium, city, day
    for row in data:
        r = random.uniform(0, 1)
        if r > pm:
            stadiums = [TEAMS[row[0]][0], TEAMS[row[1]][0]]
            std_choice = ""
            if row[2] == stadiums[0]:
                std_choice = stadiums[0]
            else:
                std_choice = stadiums[1]
            row[2] = std_choice
            row[3] = STADIUMS[std_choice][0]
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
    firstSum = 0.0
    secondSum = 0.0
    for index, gene in enumerate(row):
        #match = team1, team2, stadium, city, day
        if index == 0:
            c = T_BM1[gene]
        elif index == 1:
            c = T_BM1[gene]
        elif index == 2:
            c = S_BM1[gene]
        elif index ==3:
            c = C_BM1[gene]
        else:
            c = D_BM1[gene]
        firstSum += c ** 2.0
        secondSum += math.cos(2.0 * math.pi * c)
    n = float(len(row))
    return -20.0 * math.exp(-0.2 * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + 20 + math.e

def benchmarkFunc2(row):
    #Chung Reynolds Function
    firstSum = 0.0
    for index, gene in enumerate(row):
        #match = team1, team2, stadium, city, day
        if index == 0:
            c = T_BM2[gene]
        elif index == 1:
            c = T_BM2[gene]
        elif index == 2:
            c = S_BM2[gene]
        elif index ==3:
            c = C_BM2[gene]
        else:
            c = D_BM2[gene]
        firstSum += c ** 2.0
    return firstSum ** 2

def benchmarkFunc3(row):
    #Schumer Steiglitz Function
    firstSum = 0.0
    for index, gene in enumerate(row):
        #match = team1, team2, stadium, city, day
        if index == 0:
            c = T_BM2[gene]
        elif index == 1:
            c = T_BM2[gene]
        elif index == 2:
            c = S_BM2[gene]
        elif index ==3:
            c = C_BM2[gene]
        else:
            c = D_BM2[gene]
        firstSum = c ** 4
    return firstSum

def benchmarkFunc4(row):
    #Zigzag Function
    firstSum = 0.0
    for index, gene in enumerate(row):
        #match = team1, team2, stadium, city, day
        if index == 0:
            c = T_BM3[gene]
        elif index == 1:
            c = T_BM3[gene]
        elif index == 2:
            c = S_BM3[gene]
        elif index ==3:
            c = C_BM3[gene]
        else:
            c = D_BM3[gene]
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
    for index, gene in enumerate(row):
        #match = team1, team2, stadium, city, day
        if index == 0:
            c = T_BM1[gene]
        elif index == 1:
            c = T_BM1[gene]
        elif index == 2:
            c = S_BM1[gene]
        elif index ==3:
            c = C_BM1[gene]
        else:
            c = D_BM1[gene]
        firstSum += abs(c)
        secondSum *= abs(c)
    return firstSum + secondSum

def genetic_algo():
    POP_SIZE = 0
    data, POP_SIZE = generate_first_solution()
    fit = []
    xaxis = list(range(0, 100))
    yaxis1 = []
    yaxis2 = []
    yaxis3 = []
    yaxis4 = []
    yaxis5 = []
    for row in data:
        fit.append(fitness(row))
    print(data[0], 1/fit[0])
    print("\n")
    for iterations in range(100):
        #print(data)
        tt = data.copy()
        print("\t\t\t***** Iteration Number " + str(iterations) + " *****")
        new_population = reproduce(data, 0.9)
        new_population = variate(new_population, 0.01)
        fit = []
        for row in new_population:
            fit.append(fitness(row))
        temp = select_pop(new_population, fit, POP_SIZE)
        data = []
        data, fit = temp[0], temp[1]
        print("is data same " + str(data == tt))
        print(data[0], 1/fit[0])
        print("\n")
        yaxis1.append(benchmarkFunc1(data[0]))
        yaxis2.append(benchmarkFunc2(data[0]))
        yaxis3.append(benchmarkFunc3(data[0]))
        yaxis4.append(benchmarkFunc4(data[0]))
        yaxis5.append(benchmarkFunc5(data[0]))
    print(data[0], 1/fit[0])
    figure, axis = plt.subplots(3, 2)
    axis[0, 0].plot(xaxis, yaxis1)
    axis[0, 0].set_title("Ackley 1 Function")
    axis[0, 1].plot(xaxis, yaxis2)
    axis[0, 1].set_title("Chung Reynolds Function")
    axis[1, 0].plot(xaxis, yaxis3)
    axis[1, 0].set_title("Schumer Steiglitz Function")
    axis[1, 1].plot(xaxis, yaxis4)
    axis[1, 1].set_title("Zigzag Function")
    axis[2, 0].plot(xaxis, yaxis5)
    axis[2, 0].set_title("SSchwefel 2.22 Function")
    plt.show()
    return

genetic_algo()
