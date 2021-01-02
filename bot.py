import tweepy
from lyricsgenius import Genius
import random
import os
import json

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.getenv('OAUTH1'), os.getenv('OAUTH2'))
auth.set_access_token(os.getenv('ACCESS1'), os.getenv('ACCESS2'))

# Authenticate to Genius
genius = Genius(os.getenv('GENIUS'))

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# Create and open JSON file with artist data
"""
artist = genius.search_artist("Thao & The Get Down Stay Down")
artist.save_lyrics()
"""
with open('Lyrics_ThaoTheGetDownStayDown.json') as f:
  data = json.load(f)

"""
for song in data["songs"]:
    print(song["title"])
"""

# Get random song
length = len(data["songs"])
songNum = random.randint(0, length-1)
song = data["songs"][songNum]

# Get list of song lyrics
lyrics = song["lyrics"]
lines = lyrics.split("\n")
lineNum = random.randint(0, len(lines)-4)

tweet = ""

# Compose a tweet consisting of four lines, separated by "/"
for x in range(4):
    
    # Exclude empty lines and headings like "[CHORUS]" and "[VERSE]"
    while(lines[lineNum] == "" or (lines[lineNum][0] == "[")):
        lineNum += 1
    
    if len(tweet + lines[lineNum] + " / ") < 280:
        tweet += lines[lineNum] + " / "

    lineNum += 1

# Remove final slash
tweet = tweet[:(len(tweet)-3)]
print(tweet)

# Tweet lyrics
api.update_status(tweet)