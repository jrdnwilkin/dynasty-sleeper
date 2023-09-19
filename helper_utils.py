from copy import copy
from sleeper_wrapper import Players

def get_starters(roster):
    return roster['starters']

def get_ir(roster):
    return roster['reserve']

def get_taxi(roster):
    return roster['taxi']

def get_bench_players(roster):
    bench_players = copy(roster['players'])

    #Remove Starters
    starter_players = get_starters(roster)
    if starter_players:
        for starter in starter_players:
            if starter != '0':
                bench_players.remove(starter)

    return bench_players

def get_nfl_players():
    players = Players()
    return players.get_all_players()

