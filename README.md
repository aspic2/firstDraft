# Fantasy Sports Algorithm #

OO Python application to help you select players for fantasy sports teams.

FirstDraft was my first foray into Test Driven Development (TDD).
Please check out my file "journal.md" to hear my thoughts on how it went!


### How do I get set up? ###
This project is pure python 3. No additional packages needed.
It runs on the command line, but I have noticed some issues with the packages
when running it in Bash vs. my IDE. If you run into some "module not found" 
errors, try scanning the project for "firstDraft." import statements and remove
the "firstDraft." part. (e.g. "from firstDraft.team import Team" becomes
"from team import Team").


### Using the Program ###
In the main.py module, specify the number of rounds you want to play. NFL.com 
default is 15 rounds. Then, run main.py.

You will be prompted to input:
  - Number of teams
  - Name for each team
  - Whether or not each team will be a bot (automated strategy)
  
Bot teams handle all their own picks, and quickly. Manual teams will be
presented with a list of choices to perform for each round. Simply follow
the input instructions and you should have your winning team in no time!


### Logic ###
This program relies on a few heuristics on how best to select fantasy players.
The one I stuck with was the position standard deviation strategy. In short, 
rather than picking all the players with the highest points, you should pick
players from the positions with the highest disparity in points first. This is 
what the auto-select option uses, and it is accessible through the manual
selection process.
 
All return_options() functions return the top 10 players from the filter, just
to prevent overwhelming the user.


# Incomplete Tasks #
Below are few things I need to build or clean up in the project.

* ~~User interface: allow Team to pick() players from list~~
* Fully automate tests (meaning skip the user-input stuff when testing)
* Better error-handling for invalid user inputs
* normalize inputs to .upper() or .lower()
* auto-select feature along with repo.remove() functionality
* fix paths and "module not found" errors when running this outside IDEs
* ~~UI: for each team in Draft.draft() re-do if selection is invalid~~
* ~~AI: automated strategy option for team~~
* ~~UI: remove players without them being drafted (for real-life simulation)~~
* ~~PlayerRepo() or Team() add standard deviation for positions.~~
* ~~Player() connect to database to build real players~~
* ~~Team() view available players and stats. (Maybe return from player_repo)~~

* Source for rules and data points
	- I used the following links to find out how to rate players for your team
	and to get corresponding data points
		- Scoring settings - http://www.nfl.com/fantasyfootball/help/nfl-scoringsettings#settings
		- NFL stats by player position - http://www.nfl.com/stats/categorystats?tabSeq=1&statisticPositionCategory=QUARTERBACK&qualified=true&season=2010&seasonType=REG
		- better stats by player position - http://fantasy.nfl.com/research/players
		- list of all players - http://www.nfl.com/players/search

### Further steps ###

A few other heuristics that I would like to add:
  - Select best player available, regardless of position, provided quotas are met
  - More sophisticated handling of quotas. (Currently tries to fill all quotas
  first, then gets best player for each position)
    - I think there is an upper limit for positions after which the shift to other
    positions should be made, provided all the best players are mostly in
    one position.
  - Random selection, just for fun!
  
Also, I want to look into other data points to make predictions. 
No ideas yet for this

### Report Bugs ### 

I am aware of quite a few bugs with this program. (see incomplete tasks section).
If you come across something that I didn't mention above, feel free to point it
out here, and I'll try to get to it as soon as I can. 

### License ###

Please check the included license to determine how you may this program.
