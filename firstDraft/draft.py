
from firstDraft.team import Team
from firstDraft.player_repo import PlayerRepo


class Draft(object):

    def __init__(self, teams_list):
        self.teams = teams_list
        self.repo = PlayerRepo().fill_list()

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
        pass

