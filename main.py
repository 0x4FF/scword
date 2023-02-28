import requests
import json
from colorama import Fore
import os

client_id = ""
  
def user_scrape():
  try:
    os.unlink("results.txt")
  except:
    pass
  target = input("Enter Keyword: ")
  search_result_json = requests.get(f"https://api-mobile.soundcloud.com/search/users?q={target}&limit=200&client_id={client_id}")
  record = json.loads(search_result_json.text)

  count=0
  for records in record['collection']:
    with open("results.txt", "a") as result_file:
      count+=1
      try:
        result_file.write(f"""
{Fore.GREEN}==================={Fore.RESET}
Record: #{count}
Display Name: {record['collection'][count]['username']}

Avatar: {record['collection'][count]['avatar_url']}
Link: https://soundcloud.com/{record['collection'][count]['permalink']}
Tracks: {record['collection'][count]['tracks_count']}
Followers: {record['collection'][count]['followers_count']}
Following: {record['collection'][count]['followings_count']}
Creation Date: {record['collection'][count]['created_at']}
Bio: {record['collection'][count]['description']}  
{Fore.GREEN}==================={Fore.RESET}   
""")
      except KeyError:
        pass
      except IndexError:
        pass
        
def song_scrape():
  try:
    os.unlink("results.txt")
  except:
    pass
  target = input("Enter Keyword: ")
  search_result_json = requests.get(f"https://api-mobile.soundcloud.com/search/tracks?q={target}&limit=200&client_id={client_id}")
  record = json.loads(search_result_json.text)

  counts = 0
  for records in record['collection']:
    with open("results.txt", "a") as result_file:
      counts += 1
      try:
        result_file.write(f"""
{Fore.GREEN}======================================={Fore.RESET}
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
{Fore.GREEN}==================================================={Fore.RESET} 
""")
      except KeyError:
        pass
      except IndexError:
        print("done.")


def main():
  choice = input("[1] Scrape Profile    [2] Scrape Tracks: ")
  if choice == "1":
    user_scrape()
  elif choice == "2":
    song_scrape()
if __name__ == "__main__":
  main()
