
class Footballer:
    def __init__(self, name="UNK", start_rank=0, wins=0, losses=0, draws=0, points=0):
        self.name = name
        self.start_rank = start_rank
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points

        # self.overall_rank = self.start_rank + points
        # self.matches = wins+losses+draws
        # try:
        #     self.victory_rate = self.wins / self.matches
        # except:
        #     self.victory_rate = 0
