# groups together all modules and runs full draft

# TODO: Create free draft option for one player. Free Draft allows user to
# TODO: use all filters, draft players mark any player as unavailable at any point

from firstDraft.draft import Draft
from firstDraft.team import Team


def run_draft():
    """Specify how many rounds you want to have in Draft(number_of_rounds)"""
    draft = Draft(15).start()
    return draft

if __name__ == '__main__':
    run_draft()


