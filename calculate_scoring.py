from sleeper_wrapper import League
from sleeper_wrapper import Stats
import json

league_id = 784093541424111616
season = 2022 #We are expecting rule changes regarding this in 2023 (such as expecting unique number of replacements and using !didPlayerScoreZero instead of didPlayerScoreMoreThanZero)

week = 8

stats = Stats()
league = League(league_id)
rosters = league.get_rosters()
scoring_settings = league.get_league()['scoring_settings']

week_stats = stats.get_week_stats("regular", season, week)

def get_player_week_score(player_id):
    if player_id in week_stats:
        player_stats = week_stats[player_id]
        points = 0

        # Calculate points from scoring_settings
        for stat in player_stats:
            if stat in scoring_settings:
                points = points + (player_stats[stat] * scoring_settings[stat])

        # Round to nearest hundreth (needed due to float)
        return round(points,2)
    return 0

def get_roster_scoring(roster):
    scores = {}
    for player_id in roster['players']:
        points = get_player_week_score(player_id)
        scores[player_id] = points
    return scores
        

def check_league():
    week_scoring = {}
    for roster in rosters:
        week_scoring.update(get_roster_scoring(roster))

    with open('scoring.json', 'w') as scoringFile:
        json.dump(week_scoring, scoringFile)

check_league()