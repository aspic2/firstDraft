
from firstDraft.team import Team
from firstDraft.player_repo import PlayerRepo


class Draft(object):

    def __init__(self, rounds=5, teams=[]):
        """Creates the Draft and everything needed to run the program"""
        self.teams = teams
        self.repo = PlayerRepo().populate_repo().sort_repo().populate_dict()
        # default to 15, as this is the nfl.com standard
        self.rounds = rounds

    def round_of_drafts(self):
        """Cycle through each team in draft to make sure each gets to draft."""
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
            count = 1
            total_teams = int(input("How many teams? "))
            while count <= total_teams:
                name = input("Team " + str(count) + " name: ")
                bot = input("Is this a bot? Enter Y or N: ")
                if bot.lower() == "n":
                    self.teams.append(Team(name, False))
                else:
                    self.teams.append(Team(name))
                count += 1
        current_round = 1

        while current_round < self.rounds + 1:
            self.round_of_drafts()
            current_round += 1
        return self

    def show_standings(self):
        for team in self.teams:
            point_sum = 0
            print(team.owner + "'s current roster:\n")
            print(str(len(team)) + " current players")
            for player in team:
                print(player.name, player.position, player.points)
                point_sum += player.points
            print("----------------------------------")
        return self

