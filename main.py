from requests import get
from json import loads, load
from sys import argv
import argparse

with open('config.json', 'r+') as file:
  config = load(file)
  client_id = config["id"]
  
def user_scrape():
  target = argv[2]
  search_result_json = get(f"https://api-mobile.soundcloud.com/search/users?q={target}&limit=200&client_id={client_id}")
  record = loads(search_result_json.text)

  for count,records in enumerate(record['collection'],0):
    with open("results.txt", "a") as result_file:
      try:
        result_file.write(f"""
===================
Record: #{count}
Display Name: {record['collection'][count]['username']}

Avatar: {record['collection'][count]['avatar_url']}
Link: https://soundcloud.com/{record['collection'][count]['permalink']}
Tracks: {record['collection'][count]['tracks_count']}
Followers: {record['collection'][count]['followers_count']}
Following: {record['collection'][count]['followings_count']}
Creation Date: {record['collection'][count]['created_at']}
Bio: {record['collection'][count]['description']}  
=================== 
""")
      except KeyError:
        pass
      except IndexError:
        pass
        
def song_scrape():
  target = argv[2]
  search_result_json = get(f"https://api-mobile.soundcloud.com/search/tracks?q={target}&limit=200&client_id={client_id}")
  record = loads(search_result_json.text)
  for counts,records in enumerate(record['collection'],0):
    with open("results.txt", "a") as result_file:
      try:
        result_file.write(f"""
=======================================
Record: #{counts}
Title: {str(record['collection'][counts]['title'])}

Uploaded: {record['collection'][counts]['created_at']}
Link: {record['collection'][counts]['permalink_url']}
Duration: {record['collection'][counts]['full_duration']}
Availability: {record['collection'][counts]['sharing']}
Waveform: {record['collection'][counts]['waveform_url']}
Likes: {record['collection'][counts]['_embedded']['stats']['likes_count']}
Plays: {record['collection'][counts]['_embedded']['stats']['playback_count']} 

Description: {record['collection'][counts]['description']}  
=================================================== 
""")
      except KeyError:
        pass
      except IndexError:
        print("done.")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", help="Scrape profiles referencing the keyword")
  parser.add_argument("-t", help="Scrape tracks referencing the keyword")
  cli_args = parser.parse_args()
  if cli_args.p:
    user_scrape()
  if cli_args.t:
    song_scrape()
    
