class Data:
    TEAMS = [["Arsenal", "Emirates Stadium", "London", "Hilton"],
            ["Aston Villa", "Villa Park", "Aston", "Holiday Inn"],
            ["Blackburn", "Ewood Park", "Leamington", "Blackburn Hotel"],
            ["Chelsea", "Stamford Bridge", "Fulham", "Millennium & Copthorne"],
            ["Everton", "Goodison Park", "Walton", "Dixie Dean"],
            ["Liverpool", "Anfield", "Merseyside", "Hope Street"],
            ["Machester Utd", "Old Trafford", "Old Trafford", "Hyatt"],
            ["Manchester City", "Etihad Stadium", "East Manchester", "Emirates Palace"],
            ["Southampton", "St Mary's", "Southampton", "Jury's Inn"],
            ["Tottenham", "Tottenham Hotspur", "North London", "Myddelton Lodge"]]
    HOTELS = [["Arsenal", 6250, "London", "Hilton"],
            ["Aston Villa", 5435, "Aston", "Holiday Inn"],
            ["Blackburn", 5676, "Leamington", "Blackburn Hotel"],
            ["Chelsea", 3000, "Fulham", "Millennium & Copthorne"],
            ["Everton", 2500, "Walton", "Dixie Dean"],
            ["Liverpool", 6500, "Merseyside", "Hope Street"],
            ["Machester Utd", 4000, "Old Trafford", "Hyatt"],
            ["Manchester City", 4565, "East Manchester", "Emirates Palace"],
            ["Southampton", 5500, "Southampton", "Jury's Inn"],
            ["Tottenham", 6500, "North London", "Myddelton Lodge"]]
    STADIUMS = [["Emirates Stadium", 60260],
                ["Villa Park", 42785],
                ["Ewood Park", 31367],
                ["Stamford Bridge", 41837],
                ["Goodison Park", 39572],
                ["Anfield", 53394],
                ["Old Trafford", 76000],
                ["Etihad Stadium", 55097],
                ["St Mary's", 32505],
                ["Tottenham Hotspur", 62850]]
    ROUTES = [["London", "Aston", 2200],
            ["London", "Leamington", 8100],
            ["London", "Fulham", 3600],
            ["London", "Walton", 1500],
            ["London", "Merseyside", 22180],
            ["London", "Old Trafford", 19990],
            ["London", "East Manchester", 21120],
            ["London", "Southampton", 8000],
            ["London", "North London", 400],
            ["Aston", "Leamington", 3720],
            ["Aston", "Fulham", 10100],
            ["Aston", "Walton", 3190],
            ["Aston", "Merseyside", 9620],
            ["Aston", "Old Trafford", 8580],
            ["Aston", "East Manchester", 2240],
            ["Aston", "Southampton", 14360],
            ["Aston", "North London", 11820],
            ["Leamington", "Fulham", 1180],
            ["Leamington", "Walton", 2400],
            ["Leamington", "Merseyside", 12980],
            ["Leamington", "Old Trafford", 11920],
            ["Leamington", "East Manchester", 11970],
            ["Leamington", "Southampton", 11260],
            ["Leamington", "North London", 1220],
            ["Fulham", "Walton", 1700],
            ["Fulham", "Merseyside", 17707],
            ["Fulham", "Old Trafford", 20800],
            ["Fulham", "East Manchester", 20840],
            ["Fulham", "Southampton", 6400],
            ["Fulham", "North London", 4000],
            ["Walton", "Merseyside", 5600],
            ["Walton", "Old Trafford", 400],
            ["Walton", "East Manchester", 19780],
            ["Walton", "Southampton", 34510],
            ["Walton", "North London", 21340],
            ["Merseyside", "Old Trafford", 3090],
            ["Merseyside", "East Manchester", 5430],
            ["Merseyside", "Southampton", 23610],
            ["Merseyside", "North London", 22140],
            ["Old Trafford", "East Manchester", 310],
            ["Old Trafford", "Southampton", 22510],
            ["Old Trafford", "North London", 21080],
            ["East Manchester", "Southampton", 22540],
            ["East Manchester", "North London", 21120],
            ["Southampton", "North London", 8270]]

    def __init__(self):
        self._teams = []
        self._routes = []
        self._hotels = []
        self._stadiums = []
        for index in range(len(self.TEAMS)):
            self._teams.append(Team(self.TEAMS[index][0], self.TEAMS[index][1], self.TEAMS[index][2], self.TEAMS[index][3]))
        for index in range(len(self.ROUTES)):
            self._routes.append(Routes(self.ROUTES[index][0], self.ROUTES[index][1], self.ROUTES[index][2]))
        for index in range(len(self.HOTELS)):
            self._hotels.append(Hotels(self.HOTELS[index][3], self.HOTELS[index][2], self.HOTELS[index][1], self.HOTELS[index][0]))
        for index in range(len(self.STADIUMS)):
            self._stadiums.append(Hotels(self.STADIUMS[index][3], self.STADIUMS[index][2], self.STADIUMS[index][1], self.STADIUMS[index][0]))

        match1 = Match("M1", "Machester Utd", "Chelsea", "Old Trafford", "Old Trafford")
        match2 = Match("M2", "Manchester City", "Everton", "Etihad Stadium", "East Manchester")
        match3 = Match("M3", "Southampton", "Arsenal", "St Mary's", "Southampton")
        match4 = Match("M4", "Arsenal", "Chelsea", "Emirates Stadium", "London")
        match5 = Match("M5", "Machester City", "Chelsea", "Etihad Stadium", "East Manchester")

        #consider the 6 elements and check the evaluation function to check the revenue


class Schedule:
    def __init__(self):
        self._data = data
        self._matches = []
        self._revenue = 0
        self._fitness = -1
        self._matchNum = 0
        self._isFitnessChanged = True

class Population:
    '''

    '''

class GeneticAlgorithm:
    '''

    '''

class Team:
    def __init__(self, name, homestadium, city, hotel):
        self._name = name
        self._city = city
        self._hotel = hotel
        self._homestadium = homestadium

    def getName(self):
        return self._name
    def getCity(self):
        return self._city
    def getHotel(self):
        return self._hotel
    def getHomestadium(self):
        return self._homestadium

class Stadium:
    def __init__(self, name, city, capacity, hometeam):
        self._name = name
        self._city = city
        self._capacity = capacity
        self._hometeam = hometeam

    def getName(self):
        return self._name
    def getCity(self):
        return self._city
    def getCapacity(self):
        return self._name
    def getHometeam(self):
        return self._city

class Routes:
    def __init__(self, source, destination, cost):
        self._source = source
        self._destination = destination
        self._cost = cost

    def getId(self):
        return self._id
    def getSource(self):
        return self._source
    def getDestination(self):
        return self._destination
    def getCost(self):
        return self._cost

class Hotels:
    def __init__(self, name, city, cost, hometeam):
        self._name = name
        self._city = city
        self._cost = cost
        self._hometeam = hometeam

    def getName(self):
        return self._name
    def getCity(self):
        return self._city
    def getCost(self):
        return self._cost
    def getHometeam(self):
        return self._hometeam

class Match:
    def __init__(self, id, team1, team2, stadium, city):
        self._id = id
        self._team1 = team1
        self._team2 = team2
        self._stadium = stadium
        self._revenue = None
        self._day = None

    def getId(self):
        return self._id
    def getTeam1(self):
        return self._team1
    def getTeam2(self):
        return self._team2
    def getStadium(self):
        return self._stadium
    def getRevenue(self):
        return self._revenue
    def getDay(self):
        return self._day
    def setId(self):
        self._id = id
    def setRevenue(self):
        self._revenue = revenue
    def setDay(self):
        self._revenue = day

data = Data()
