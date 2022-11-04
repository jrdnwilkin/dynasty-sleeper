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

    #Remove IR
    ir_players = get_ir(roster)
    if ir_players:
        for ir_player in ir_players:
            if starter != '0':
                bench_players.remove(ir_player)

    #Remove Taxi Squad
    taxi_players = get_taxi(roster)
    if taxi_players:
        for taxi_player in taxi_players:
            if starter != '0':
                bench_players.remove(taxi_player)

    return bench_players

def get_nfl_players():
    players = Players()
    return players.get_all_players()

