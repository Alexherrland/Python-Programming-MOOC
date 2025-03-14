import json

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:<21}{self.team:<4}{self.goals:>3} + {self.assists:>3} = {self.points():>3}"

class NHLStats:
    def __init__(self, filename):
        self.players = self.load_data(filename)
    
    def load_data(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Player(**player) for player in data]
        except FileNotFoundError:
            print("File not found.")
            return []
    
    def search_player(self, name):
        for player in self.players:
            if player.name.lower() == name.lower():
                print(player)
                return
        print("Player not found.")
    
    def list_teams(self):
        teams = sorted(set(player.team for player in self.players))
        print("\n".join(teams))
    
    def list_countries(self):
        countries = sorted(set(player.nationality for player in self.players))
        print("\n".join(countries))
    
    def players_in_team(self, team):
        players = sorted([p for p in self.players if p.team == team], key=lambda p: p.points(), reverse=True)
        for player in players:
            print(player)
    
    def players_from_country(self, country):
        players = sorted([p for p in self.players if p.nationality == country], key=lambda p: p.points(), reverse=True)
        for player in players:
            print(player)
    
    def top_scorers(self, n):
        players = sorted(self.players, key=lambda p: (p.points(), p.goals), reverse=True)[:n]
        for player in players:
            print(player)
    
    def top_goal_scorers(self, n):
        players = sorted(self.players, key=lambda p: (p.goals, -p.games), reverse=True)[:n]
        for player in players:
            print(player)

class NHLStatsApplication:
    def __init__(self):
        filename = input("file name: ")
        self.stats = NHLStats(filename)
        if not self.stats.players:
            return
        print(f"read the data of {len(self.stats.players)} players")
    
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.stats.search_player(input("name: "))
            elif command == "2":
                self.stats.list_teams()
            elif command == "3":
                self.stats.list_countries()
            elif command == "4":
                self.stats.players_in_team(input("team: "))
            elif command == "5":
                self.stats.players_from_country(input("country: "))
            elif command == "6":
                self.stats.top_scorers(int(input("how many: ")))
            elif command == "7":
                self.stats.top_goal_scorers(int(input("how many: ")))
            else:
                self.help()

if __name__ == "__main__":
    NHLStatsApplication().execute()
