from sleeper_wrapper import Players
import json

players = Players()

nfl_players = players.get_all_players()

with open('players.json', 'w') as playersFile:
    json.dump(nfl_players, playersFile)

