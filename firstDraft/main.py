# groups together all modules and runs full draft

from firstDraft.draft import Draft


def run_draft():
    draft = Draft().start()
    return draft

if __name__ == '__main__':
    run_draft()


