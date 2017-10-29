
from firstDraft.team import Team
from firstDraft.player_repo import PlayerRepo


class Draft(object):

    def __init__(self, rounds=15):
        self.teams = [Team("Alpha"), Team("Gold")]
        self.repo = PlayerRepo().fill_list()
        # default to 15, as this is the nfl.com standard
        self.rounds = rounds

    def round_of_drafts(self):
        for t in self.teams:
            print(t.owner + "'s Turn:")
            # TODO: fix hard-coding of selected player
            # TODO: ensure both t.draft_player() and repo.draft_player() happen!
            # TODO: potential for discrepancy in available players currently
            t.take_turn(self.repo.return_available_players())
            print(t.owner + "'s new roster is:\n")
            for p in t:
                print(p.name, p.position, p.points)
            print("\n\n")
        return self

    def start(self):
        current_round = 1
        while current_round < self.rounds + 1:
            self.round_of_drafts()
            current_round += 1
        return self

