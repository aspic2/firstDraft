# each GM builds a Team() to gain them the most points possible this season

from sys import exit


class Team(list):
    """The application's goal is to make the best Team() (i.e. the team with
    the most points by the end of the season). Class will hold roster
    (selected players), quota (minimum for each position), and logic for how
    to select the next player in a draft.
    """

    quota = {"QB": 1, "RB": 2, "WR": 2, "TE": 1, "K": 1, "DEF": 1}
    positions = ["QB", "RB", "WR", "TE", "K", "DEF"]
    strategies = ["ba", "sd", "r"]
    accepted_inputs = ["SD", "BA", "R", "DRAFT"]

    def __init__(self, owner, bot=True):
        self.owner = owner
        self.pool = None
        self.bot = bot
        self.turn = False
        self.response_dict = {}
        
    def check_quota(self):
        quota_not_met = []
        for pos in Team.positions:
            num = self.count(lambda player: player.position == pos)
            if num < Team.quota[pos]:
                quota_not_met.append(pos)
        return quota_not_met

    def draft_player(self, chosen_one):
        self.append(chosen_one)
        chosen_one.get_drafted()
        self.turn = False
        return self

    def view_options(self, options):
        """This method should return a list of player names, positions,
        and expected points for the season.
        """
        # TODO: Update this to take a specified position
        options = options[:10]
        #for o in options:
        #    print(options.index(o), o.name, o.position, o.points)
        return options

    def remove_player(self, tup, p_list):
        p = next(x for x in p_list if (
            x.name.upper(), x.position) == (tup[0].upper(), tup[1].upper()))
        if p:
            p.get_drafted()
        return self

    def take_turn(self, pool):
        """Revise method to 1) show std dev for each position:
        2) return position with highest std dev.
        3) choose best available player from position.
        Method needs to print results each step of way, and eventually
        you should build control flow in to specify what to do.
        """
        # TODO: break this into multiple methods
        self.turn = True
        if self.bot:
            self.auto_strategy(pool, "sd")
        val = None
        while self.turn:
            response = input("'cq', 'vo', or 'sd'\n> ")  # test with "sd"
            if response == 'cq':
                val = self.check_quota()
                print("Quota not met for:")
                print(val)
            elif response == 'vo':
                val = self.view_options(pool)
                for v in val:
                    print(val.index(v), v.name, v.position, v.points)
            elif response == 'sd':
                val = []
                # this is duplicate code from auto_strategy
                pos = self.check_quota()
                if pos:
                    for p in pos:
                        val.append((p, pool.standard_deviation(p)))
                    for v in val:
                        print(v[0], v[1])
                    position = max(val, key=lambda x: x[1])
                    print("selecting from", position)
                    options = pool.filter_players(position[0])
                    draftee = options[0]
                    self.draft_player(draftee)
                    print("drafting", draftee.name, draftee.position)
            # self.turn = False | turn on for testing
        return self

    def auto_strategy(self, player_list, strategy):
        """This will default to a standard deviation, best available strategy."""
        new_list = []
        # does not use check_quota for now
        need_position = self.check_quota()
        if strategy == "sd":
            for p in Team.positions:
                new_list.append((p, player_list.standard_deviation(p)))
            position = max(new_list, key=lambda x: x[1])
            options = player_list.filter_players(position[0])
            draftee = options[0]
            self.draft_player(draftee)
        return self

    def prompt(self, user_input):
        user_input = user_input.upper()
        if user_input == "Q":
            exit(0)
        else:
            return user_input






    """def user_input(self):
        print('Valid commands:\n"SD" = standard deviation for the positions\n'
              '"A" = return list of top 10 players, regardless of position\n'
              '"POSITION" returns top 10 players for specified position.' 
              '"POSITION" options are\n QB, RB, WR, TE, K, DEF\n')
        response = 42   # correct response == input("> ")
        return response
        """

        
        

