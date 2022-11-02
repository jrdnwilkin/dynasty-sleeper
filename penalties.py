from sleeper_wrapper import League
from sleeper_wrapper import User
from copy import copy
import json
import helper_utils

# region VARIABLES TO UPDATE
league_id = 784093541424111616
season = 2022 # We are expecting rule changes regarding this in 2023 
week = 8
# endregion

league = League(league_id)
rosters = league.get_rosters()
roster_positions = league.get_league()['roster_positions']

scoring_file = open('scoring.json')
scoring = json.load(scoring_file)
scoring_file.close()

def did_player_score_zero(player_id):
    points = scoring[player_id]
    if points == 0: 
        return True
    return False

def did_player_score_more_than_zero(player_id):
    points = scoring[player_id]
    if points > 0: 
        return True
    return False

def get_num_penalties(roster):
    bench_players_info = helper_utils.get_players_info(helper_utils.get_bench_players(roster))


    zero_pt_starters = list(filter(did_player_score_zero, helper_utils.get_starters(roster)))


    penalty_count = 0
    for zero_starter in zero_pt_starters:
        cannot_be_replaced = True # Assume until a bench player that qualifies is found
        
        # TODO: Add code that actually checks to see if they can be replaced by a bench player.

        # Points are easy to check but need to consider how all the position stuff works. 

        # For comparing positions: can check player positions from loading player.json file then roster['starters'] is in the same order of roster_positions to determine which places people are occupying.
        for index, key in enumerate(helper_utils.get_starters()):
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

        for player_id, bench_player_info in bench_players_info.iteritems():
            if did_player_score_zero(player_id): #Player doesn't qualify
                continue
            if bench_player_info['position'] in valid_positions: 
                cannot_be_replaced = False
                break

        # Based on the current wording of the rule, we should not consider potential roster re-positionings (see README for potential changes for more info)

        if cannot_be_replaced:
            penalty_count = penalty_count + 1

    return penalty_count


def check_league():
    for roster in rosters:
        user = User(roster['owner_id'])
        user_name = user.get_username()

        #Only test with my team rn
        if user_name != 'jrdnmcgurdin':
            continue

        num_penalties = get_num_penalties(roster)
        print('Player: {} had {} penalties in week {}'.format(user_name, num_penalties, week))

check_league()