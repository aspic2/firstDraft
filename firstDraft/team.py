# each GM builds a Team() to gain them the most points possible this season


class Team(list):
    """The application's goal is to make the best Team() (i.e. the team with
    the most points by the end of the season. Class will hold roster
    (selected players), quota (minimum for each position), and logic for how
    to select the next player in a draft."""

    quota = {"QB": 1,
             "RB": 2,
             "WR": 2,
             "TE": 1,
             "K": 1,
             "DEF": 1}

    def __init__(self, data):
        self.owner = data[0]
        
    def check_quota(self, positions):
        quota_not_met = []
        for pos in positions:
            num = self.count(lambda player: player.position == pos)
            if num < Team.quota[pos]:
                quota_not_met.append(pos)
        return quota_not_met

    def draft_player(self, chosen_one):
        self.append(chosen_one)
        chosen_one.get_drafted()
        return self

        
        

