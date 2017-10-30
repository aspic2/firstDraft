# each GM builds a Team() to gain them the most points possible this season

from sys import exit


class Team(list):
    """Busiest Class in the program. Subclass of list() Object.
    The application's goal is to make the best Team() (i.e. the team with
    the most points by the end of the season). Object will hold roster
    (selected players), quota (minimum for each position), and logic for how
    to select the next player in a draft.
    """

    quota = {"QB": 1, "RB": 2, "WR": 2, "TE": 1, "K": 1, "DEF": 1}
    positions = ["QB", "RB", "WR", "TE", "K", "DEF"]
    strategies = ["ba", "sd", "r"]
    accepted_inputs = ["SD", "BA", "R", "DRAFT"]

    def __init__(self, owner, bot=True, test=False):
        """Bot value for automated picking. test value added to avoid loops 
        when testing.
        """
        self.owner = owner
        self.pool = None
        self.bot = bot
        self.turn = False
        self.response_dict = {}
        self.test = test
        self.draftee = None
        self.action_param = None
        
    def check_quota(self):
        """Checks self against Team.quota and returns any position where
        quota is not met.
        """
        quota_not_met = []
        for pos in Team.positions:
            num = self.count(lambda player: player.position == pos)
            if num < Team.quota[pos]:
                quota_not_met.append(pos)
        return quota_not_met

    def draft_player(self, chosen_one):
        """Marks player as drafted and ends turn."""
        self.append(chosen_one)
        chosen_one.get_drafted()
        self.turn = False
        return self

    def view_options(self, options):
        """Returns top players from list parameter options. Need to be revised
        to take altered lists and return options.
        """
        # TODO: Update this to take a specified position
        options = options[:10]
        #for o in options:
        #    print(options.index(o), o.name, o.position, o.points)
        return options

    def remove_player(self, tup, p_list):
        """Method for live drafts. Removes player from available list without
        explicitly drafting player to a team.
        """
        p = next(x for x in p_list if (
            x.name.upper(), x.position) == (tup[0].upper(), tup[1].upper()))
        if p:
            p.get_drafted()
        return self

    def take_turn(self, pool):
        """Loop method to keep prompting user for input until user drafts."""
        full_player_list = pool
        parameter = "quota"
        self.turn = True
        """Logic for automated picking"""
        if self.bot:
            self.auto_strategy(pool, "sd")
        elif self.test:
            param = input("> ")
            self.actions(full_player_list, param)
            self.turn = False
        else:
            while self.turn:
                print("valid actions: quota, options, sd, filter, find, draft, remove, end turn")
                # It's gettin' functional up in here!
                param = input("> ")
                self.actions(full_player_list, param)
        return self

    def actions(self, pool, response):
        """Sloppy method to handle user input and return or print 
        appropriate values. 
        
        This method needs to be simplified and
        have proper unit tests built for it.
        
        Additionally, input needs to be normalized for capitalization.
        """
        val = None
        draftee = None
        # TODO: Make a function that can use default values when testing
        # response = "sd"  # input("'quota', 'options', 'sd', or 'draft'\n> ")  # test with "sd"
        if response == 'quota':
            val = self.check_quota()
            print("Quota not met for:")
            print(val)
            return val
        # TODO: Make this show only players that meet certain restrictions
        # TODO: Currently shows best of all players only
        elif response == 'options':
            val = self.view_options(pool)
            for v in val:
                print(val.index(v), v.name, v.position, v.points)
        elif response == 'sd':
            val = []
            for p in self.positions:
                val.append((p, pool.standard_deviation(p)))
            # TODO: added sort. need to add test for the sort
            val.sort(key=lambda x: x[1], reverse=True)
            for v in val:
                print(v[0], v[1])
        elif response == 'filter':
            position = input("Select position to choose from\n> ")
            print("selecting from", position)
            options = pool.filter_by_position(position)
            for o in options:
                print(options.index(o), o.name, o.position, o.points)
        elif response == 'find':
            self.draftee = pool.return_player(self.find_player())
        elif response == 'draft':
            print("drafting", self.draftee.name, self.draftee.position)
            self.draft_player(self.draftee)
            self.reset_draftee()
        elif response == 'remove':
            print("removing", self.draftee.name, self.draftee.position)
            self.draftee.get_drafted()
            self.reset_draftee()
        elif response == 'end turn':
            self.reset_draftee()
            self.turn = False
        else:
            print("Action not recognized. Please enter a valid action.")
        # self.turn = False | turn on for testing
        if self.draftee:
            print("You currently have draftee", self.draftee.name, self.draftee.position)
            # print("drafting", draftee.name, draftee.position)
            # self.draft_player(draftee)
        return val

    def auto_strategy(self, player_list, strategy):
        """This will default to a standard deviation, best available strategy."""
        new_list = []
        # does not use check_quota for now
        need_position = self.check_quota()
        if strategy == "sd":
            for p in Team.positions:
                new_list.append((p, player_list.standard_deviation(p)))
            position = max(new_list, key=lambda x: x[1])
            options = player_list.filter_by_position(position[0])
            draftee = options[0]
            self.draft_player(draftee)
        return self

    # TODO: This module is unused (except for its test)
    def user_input(self, prompt):
        user_input = prompt.upper()
        if user_input == "Q":
            exit(0)
        else:
            return user_input

    def find_player(self):
        """Returns tuple(name, position) value to PlayerRepo.return_player()"""
        print('Which player would you like to find?')
        print('Enter "FIRSTNAME LASTNAME", press enter, then enter "POSITION"')
        if self.test:
            name = "Drew Brees"
            position = "QB"
        else:
            name = input("name: ")
            position = input("position: ")
        n_and_p = (name, position)
        print(n_and_p)
        return n_and_p

    def reset_draftee(self):
        """self.draftee is used to control some logic flow and, as such
        needs to be reset after each turn.
        """
        self.draftee = None
        return self
