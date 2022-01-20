import math
import random

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
HOTELS = {"Arsenal": [6250, "London", "Hilton"],
            "Aston Villa": [5435, "Aston", "Holiday Inn"],
            "Blackburn": [5676, "Leamington", "Blackburn Hotel"],
            "Chelsea": [3000, "Fulham", "Millennium & Copthorne"],
            "Everton": [2500, "Walton", "Dixie Dean"],
            "Liverpool": [6500, "Merseyside", "Hope Street"],
            "Machester Utd": [4000, "Old Trafford", "Hyatt"],
            "Manchester City": [4565, "East Manchester", "Emirates Palace"],
            "Southampton": [5500, "Southampton", "Jury's Inn"],
            "Tottenham": [6500, "North London", "Myddelton Lodge"]}
STADIUMS = {"Emirates Stadium": ["London", 60260],
                "Villa Park": ["Aston",42785],
                "Ewood Park": ["Leamington",31367],
                "Stamford Bridge": ["Fulham",41837],
                "Goodison Park": ["Walton",39572],
                "Anfield": ["Merseyside",53394],
                "Old Trafford": ["Old Trafford",76000],
                "Etihad Stadium": ["East Manchester",55097],
                "St Mary's": ["Southampton",32505],
                "Tottenham Hotspur": ["North London",62850]}
ROUTES = {("London", "Aston"): 2200,
            ("London", "Leamington"): 8100,
            ("London", "Walton"): 1500,
            ("London", "Fulham"): 3600,
            ("London", "Merseyside"): 22180,
            ("London", "Old Trafford"): 19990,
            ("London", "East Manchester"): 21120,
            ("London", "Southampton"): 8000,
            ("London", "North London"): 400,
            ("Aston", "Leamington"): 3720,
            ("Aston", "Fulham"): 10100,
            ("Aston", "Walton"): 3190,
            ("Aston", "Merseyside"): 9620,
            ("Aston", "Old Trafford"): 8580,
            ("Aston", "East Manchester"): 2240,
            ("Aston", "Southampton"): 14360,
            ("Aston", "North London"): 11820,
            ("Leamington", "Fulham"): 1180,
            ("Leamington", "Walton"): 2400,
            ("Leamington", "Merseyside"): 12980,
            ("Leamington", "Old Trafford"): 11920,
            ("Leamington", "East Manchester"): 11970,
            ("Leamington", "Southampton"): 11260,
            ("Leamington", "North London"): 1220,
            ("Fulham", "Walton"): 1700,
            ("Fulham", "Merseyside"): 17707,
            ("Fulham", "Old Trafford"): 20800,
            ("Fulham", "East Manchester"): 20840,
            ("Fulham", "Southampton"): 6400,
            ("Fulham", "North London"): 4000,
            ("Walton", "Merseyside"): 5600,
            ("Walton", "Old Trafford"): 400,
            ("Walton", "East Manchester"): 19780,
            ("Walton", "Southampton"): 34510,
            ("Walton", "North London"): 21340,
            ("Merseyside", "Old Trafford"): 3090,
            ("Merseyside", "East Manchester"): 5430,
            ("Merseyside", "Southampton"): 23610,
            ("Merseyside", "North London"): 22140,
            ("Old Trafford", "East Manchester"): 310,
            ("Old Trafford", "Southampton"): 22510,
            ("Old Trafford", "North London"): 21080,
            ("East Manchester", "Southampton"): 22540,
            ("East Manchester", "North London"): 21120,
            ("Southampton", "North London"): 8270}


def generate_first_solution():
    data = []
    #match = team1, team2, stadium, city, day
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
            data.append(temp)

    #print(len(data))
    #print(data)
    return data

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
    return ticket_revenue - travel_exp - hotel_exp

def fitness(row):
    result = evaluation(row)
    if row == 0:
        return 10 ** 6
    else:
        return (1 / result)

data = generate_first_solution()
print(data)
