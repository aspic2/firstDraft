
from firstDraft.team import Team
from firstDraft.player_repo import PlayerRepo


class Draft(object):

    def __init__(self):
        self.teams = [Team("Alpha"), Team("Gold")]
        self.repo = PlayerRepo().fill_list()
        # default to 15, as this is the nfl.com standard
        self.number_of_rounds = 15

    def round_of_drafts(self):
        for t in self.teams:
            # TODO: fix hard-coding of selected player
            # TODO: ensure both t.draft_player() and repo.draft_player() happen!
            # TODO: potential for discrepancy in available players currently
            draft_candidate = self.repo[0]
            t.draft_player(self.repo[0])
            self.repo.draft_player(draft_candidate)
        return self

    def start(self):
        current_round = 1
        while current_round < self.number_of_rounds + 1:
            self.round_of_drafts()
            current_round += 1
        return self

