from sleeper_wrapper import User
import helper_utils

def did_player_score_zero(player_id, scoring):
    points = 0
    if player_id in scoring:
        points = scoring[player_id]
    if points == 0: 
        return True
    return False

def did_player_score_more_than_zero(player_id, scoring):
    points = scoring[player_id]
    if points > 0: 
        return True
    return False

def score_zero_filter(scoring):
   def myfilter(player_id):
       return did_player_score_zero(player_id, scoring)
   return myfilter

def get_penalized_starters(roster, scoring, roster_positions, nfl_players):
    bench_players = helper_utils.get_bench_players(roster)
    zero_pt_starters = list(filter(score_zero_filter(scoring), helper_utils.get_starters(roster)))

    peanlized_starters = []
    for zero_starter in zero_pt_starters:
        cannot_be_replaced = True # Assume until a bench player that qualifies is found

        for index, key in enumerate(helper_utils.get_starters(roster)):
            if key == zero_starter:
                roster_position = roster_positions[index]
                break

        valid_positions = []
        if roster_position == "FLEX":
            valid_positions = ["RB", "WR", "TE"]
        elif roster_position == "SUPERFLEX":
            valid_positions = ["RB", "WR", "TE", "QB"]
        else: 
            valid_positions = [roster_position]

        for bench_player_id in bench_players:
            bench_player_info = nfl_players[bench_player_id]
            if did_player_score_zero(bench_player_id, scoring): #Player doesn't qualify
                continue
            for position in bench_player_info['fantasy_positions']:
                if position in valid_positions: 
                    cannot_be_replaced = False
                    break

        # Based on the current wording of the rule, we should not consider potential roster re-positionings (see README for potential changes for more info)

        if cannot_be_replaced:
            peanlized_starters.append(zero_starter)

    return peanlized_starters


def get_penalties(league, rosters, scoring):
    roster_positions = league.get_league()['roster_positions']

    penalties = {}

    nfl_players = helper_utils.get_nfl_players()

    for roster in rosters:
        user = User(roster['owner_id'])
        user_name = user.get_username()

        penalized_starters = get_penalized_starters(roster, scoring, roster_positions, nfl_players)

        penalized_starter_names = []
        for penalized_starter in penalized_starters:
            penalized_starter_names.append(nfl_players[penalized_starter]['full_name'])
        user_penalties = {'number': len(penalized_starters), 'penalized_players': penalized_starter_names}
        
        penalties[user_name] = user_penalties

    return penalties