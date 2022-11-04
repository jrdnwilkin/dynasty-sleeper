import json
from gcloud import storage

def get_or_build_weekly_roster(league, week):
    client = storage.Client(project='sleeper-dynasty')
    bucket = client.get_bucket('sleeper-dynasty-nfl-empire-wars')

    season = league.get_league()['season']
    gcloud_file_path = 'data/{}/{}.json'.format(season, week)

    existing_blob = bucket.get_blob(gcloud_file_path)
    if existing_blob is None: # upload to google cloud
        with open('/tmp/rosters.json', 'w') as rosters_file:
            rosters = league.get_rosters()
            json.dump(rosters, rosters_file)
        blob = bucket.blob(gcloud_file_path)
        blob.upload_from_filename(filename='/tmp/rosters.json')
        return rosters
    else: # download from google cloud
        existing_blob.download_to_filename(filename='/tmp/rosters.json')

        rosters_file = open('/tmp/rosters.json')
        rosters = json.load(rosters_file)
        rosters_file.close()
        return rosters


    