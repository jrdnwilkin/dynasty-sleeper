from sleeper_wrapper import Stats

def get_player_week_score(player_id, scoring_settings, week_stats):
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

def get_roster_scoring(roster, scoring_settings, week_stats):
    scores = {}
    for player_id in roster['players']:
        points = get_player_week_score(player_id, scoring_settings, week_stats)
        scores[player_id] = points
    return scores
        

def calculate_and_build_scoring(league, rosters, week):
    stats = Stats()
    league_dict = league.get_league()
    scoring_settings = league_dict['scoring_settings']

    week_stats = stats.get_week_stats("regular", league_dict['season'], week)

    week_scoring = {}
    for roster in rosters:
        week_scoring.update(get_roster_scoring(roster, scoring_settings, week_stats))

    return week_scoring

