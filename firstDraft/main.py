"""Cleaner module from which to run the application."""

from firstDraft.draft import Draft


def run_draft(number_of_rounds):
    draft = Draft(number_of_rounds).start().show_standings()
    return draft

if __name__ == '__main__':
    """NFL.com default is 15 rounds."""
    run_draft(10)


