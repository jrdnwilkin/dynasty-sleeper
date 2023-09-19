from sleeper_wrapper import League
import scoring
import penalties
import emailer
import os
from dotenv import load_dotenv

def handler(_loud_param1, cloud_param2):
    week = 1
    email_address = 'jrdnwilkin+testreceive@gmail.com' #SET EMAIL ADDRESS
    league_id=os.environ.get('LEAGUE_ID')
    current_league = League(league_id)

    week_matchups = current_league.get_matchups(week)
    week_scoring = scoring.calculate_and_build_scoring(current_league, week_matchups, week)

    week_penalties = penalties.get_penalties(current_league, week_matchups, week_scoring)

    print(week_penalties)
    emailer.email_results(week_penalties, email_address, week)
