from utility import calc_factorial
import random

class Footballer:
    def __init__(self, name="UNK", start_rank=0, wins=0, losses=0, draws=0):
        self.name = name
        self.start_rank = start_rank
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = start_rank+wins-losses

        # self.overall_rank = self.start_rank + points
        # self.matches = wins+losses+draws
        # try:
        #     self.victory_rate = self.wins / self.matches
        # except:
        #     self.victory_rate = 0


available_players_pool = [
Footballer(name="Bonfa", start_rank=2),
Footballer(name="Karim", start_rank=3),
Footballer(name="Mor", start_rank=3),
Footballer(name="Akil", start_rank=3),
Footballer(name="Duccio", start_rank=1),
Footballer(name="Philipp", start_rank=3),
Footballer(name="Francesco collega", start_rank=3),
Footballer(name="Blallo", start_rank=2),
Footballer(name="Gio", start_rank=3),
Footballer(name="Pezzo", start_rank=3),
Footballer(name="Yarru", start_rank=3),
Footballer(name="Sboben", start_rank=5),
Footballer(name="Moataz", start_rank=3),
Footballer(name="Zebib", start_rank=2),
]

def teams_combinations(people, people_per_team) -> int:
    numerator = calc_factorial(people)
    denominator = calc_factorial(people_per_team) * calc_factorial(people-people_per_team)
    return numerator/denominator/2

def rank_of_list(lst) -> int:
    match_rank=0
    for pl in lst:
        match_rank = pl.points + match_rank
    return match_rank

def make_teams(lst) -> tuple[list, list]:
    match_rank=rank_of_list(lst)
    while True:
        team_a = random.sample(lst, int(len(lst) / 2))
        team_b = [x for x in lst if x not in team_a]
        if abs(rank_of_list(team_a) - rank_of_list(team_b)) <= 1:
            return team_a, team_b
    
def print_teams_and_stats(team_a:list, team_b:list) -> str:
    
    # team_a_player = tuple[list, list]
    # team_b_names = []
    
    text_a, text_b = "", ""
    for pl in team_a:
        # team_a_player.append(pl.name)
        text_a = text_a + f"{pl.name} ({pl.points})\n"
    for pl in team_b:
        # team_b_names.append(pl.name)
        text_b = text_b + f"{pl.name} ({pl.points})\n"

    out_text = f"----------------------------------------\nTEAM A, overall score: {rank_of_list(team_a)}\n{text_a}----------------------------------------\nTEAM B, overall score: {rank_of_list(team_b)}\n{text_b}----------------------------------------\n"
    return out_text

