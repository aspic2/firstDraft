# each GM builds a Team() to gain them the most points possible this season


class Team(list):
    """The application's goal is to make the best Team() (i.e. the team with
    the most points by the end of the season. Class will hold roster
    (selected players), quota (minimum for each position), and logic for how
    to select the next player in a draft."""

    quota = {"QB": 1, "RB": 2, "WR": 2, "TE": 1, "K": 1, "DEF": 1}

    def __init__(self, owner):
        self.owner = owner
        self.pool = None
        
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

    def view_options(self, options):
        """This method should return a list of player names, positions,
        and expected points for the season.
        """
        # make a call to player_repo to filter and/or sort the player list
        for o in options:
            print(options.index(o), o.name, o.position, o.points)
        return options

    def send_filter(self):
        """Choose from a list of filters and send to player_repo"""
        best_available = "ba"
        best_in_posiiton = "bip"
        random = "r"
        return best_available

    def take_turn(self, pool):
        """Revise method to 1) show std dev for each position:
        2) return position with highest std dev.
        3) choose best available player from position.
        Method needs to print results each step of way, and eventually
        you should build control flow in to specify what to do."""
        #draftee = int(input("Whom would you like to draft next? (Enter index only!)\n> "))
        self.draft_player(pool[draftee])
        return self

        
        

