# groups together all modules and runs full draft

# TODO: Create free draft option for one player. Free Draft allows user to
# TODO: use all filters, draft players mark any player as unavailable at any point

from firstDraft.draft import Draft


def run_draft():
    draft = Draft(15).start()
    return draft

if __name__ == '__main__':
    run_draft()


