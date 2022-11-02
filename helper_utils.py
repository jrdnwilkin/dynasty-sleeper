from copy import copy
import json

def get_player_name(player_id):
    players_file = open('players.json')
    players = json.load(players_file)
    players_file.close()

    return players[player_id]['full_name']
    

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
    for starter in starter_players:
        if starter != '0':
            bench_players.remove(starter)

    #Remove IR
    ir_players = get_ir(roster)
    for ir_player in ir_players:
        if starter != '0':
            bench_players.remove(ir_player)

    #Remove Taxi Squad
    taxi_players = get_taxi(roster)
    for taxi_player in taxi_players:
        if starter != '0':
            bench_players.remove(taxi_player)

    return bench_players

def get_players_info(player_ids):
    players_file = open('players.json')
    players = json.load(players_file)
    players_file.close()

    players_info = {}
    for player_id in player_ids:
        players_info[player_id] = players[player_id]
    return players_info
