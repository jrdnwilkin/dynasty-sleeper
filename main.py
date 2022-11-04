from sleeper_wrapper import League
import scoring
import weekly_roster
import penalties
import emailer
import os

def handler(cloud_event):

    week = 8
    email_address= 'jrdnwilkin@gmail.com'
    #email_address = 'bradly.baxter0207@gmail.com'

    current_league = League(os.environ.get('LEAGUE_ID'))
    week_rosters = weekly_roster.get_or_build_weekly_roster(current_league, week)
    week_scoring = scoring.calculate_and_build_scoring(current_league, week_rosters, week)
    
    week_penalties = penalties.get_penalties(current_league, week_rosters, week_scoring)

    print(week_penalties)
    emailer.email_results(week_penalties, email_address, week)


