import logging
from utility import calc_factorial
import random

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


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


players_pool = [
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
available_players_pool = []
# Footballer(name="Bonfa", start_rank=2),
# Footballer(name="Karim", start_rank=3),
# Footballer(name="Mor", start_rank=3),
# Footballer(name="Akil", start_rank=3),
# Footballer(name="Duccio", start_rank=1),
# Footballer(name="Philipp", start_rank=3),
# Footballer(name="Francesco collega", start_rank=3),
# Footballer(name="Blallo", start_rank=2),
# Footballer(name="Gio", start_rank=3),
# Footballer(name="Pezzo", start_rank=3),
# Footballer(name="Yarru", start_rank=3),
# Footballer(name="Sboben", start_rank=5),
# Footballer(name="Moataz", start_rank=3),
# Footballer(name="Zebib", start_rank=2),
# ]

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
    text_a, text_b = "", ""
    for pl in team_a:
        text_a = text_a + f"{pl.name} ({pl.points})\n"
    for pl in team_b:
        text_b = text_b + f"{pl.name} ({pl.points})\n"
    out_text = f"----------------------------------------\nTEAM A, overall score: {rank_of_list(team_a)}\n{text_a}----------------------------------------\nTEAM B, overall score: {rank_of_list(team_b)}\n{text_b}----------------------------------------\n"
    return out_text

def print_players_pool() -> str:
    out_text=""
    for pl in players_pool:
        out_text = out_text + f"{pl.name} ({pl.points})\n"
    print(out_text)
    return out_text

def is_player_new(new_pl:str) -> int:
    for pl in players_pool:
        if pl.name.lower() == new_pl.lower():
            logger.info(f"{new_pl} not a new player.")
            return 0
    logger.info(f"{new_pl} new player!")
    return 1

def get_player_rank(new_pl:str) -> int:
    for pl in players_pool:
        if pl.name.lower() == new_pl.lower():
            return pl.start_rank
    return 3

def insert_new_players_name(new_pl_name:str):
    players_pool.append(Footballer(name=new_pl_name, start_rank=0))

def insert_new_players_rank(new_pl_rank:int):
    name_to_insert=get_last_inserted_name()
    for pl in players_pool:
        if pl.name == get_last_inserted_name():
           players_pool.remove(pl)
    players_pool.append(Footballer(name=name_to_insert, start_rank=new_pl_rank))

def remove_uncomplete_player():
    for pl in players_pool:
        if pl.start_rank not in range (1, 6):
            players_pool.remove(pl)

def get_last_inserted_name() -> str:
    return players_pool[len(players_pool) - 1].name

def get_last_inserted_rank() -> int:
    return players_pool[len(players_pool) - 1].start_rank

## out_text = all championship stats
def print_championship_stats() -> str:
    if len(players_pool) == 0:
        out_text = f"No players are registered"
        return out_text
    out_text = f"STATISTICS OF ALL {len(players_pool)} PLAYERS:\n"
    for pl in players_pool:
        out_text = out_text + f"{pl.name} ({pl.points})\n"
    return out_text

