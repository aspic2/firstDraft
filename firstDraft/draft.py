
from firstDraft.team import Team
from firstDraft.player_repo import PlayerRepo


class Draft(object):

    def __init__(self, rounds=5, teams=[]):
        """Creates the Draft and everything needed to run the program"""
        self.teams = teams
        self.repo = PlayerRepo().fill_list().sort_repo().fill_dict()
        # default to 15, as this is the nfl.com standard
        self.rounds = rounds

    def round_of_drafts(self):
        """Cycle through each team in draft to make sure each gets to draft"""
        for t in self.teams:
            print(t.owner + "'s Turn:")
            t.take_turn(self.repo.return_available_players())
            print(t.owner + "'s new roster is:\n")
            for p in t:
                print(p.name, p.position, p.points)
            print("\n\n")
        return self

    def start(self):
        """Handle manual input for teams and auto-filled teams"""
        if not self.teams:
            count = int(input("How many teams? "))
            for num in range(count):
                name = input("Team " + str(count) + " name: ")
                bot = input("Is this a bot? Enter Y or N: ")
                if bot.lower() == "n":
                    self.teams.append(Team(name, False))
                else:
                    self.teams.append(Team(name))
        current_round = 1

        while current_round < self.rounds + 1:
            self.round_of_drafts()
            current_round += 1
        return self

