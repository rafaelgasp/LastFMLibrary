import pylast
import pandas as pd

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
username = "YOUR_USERNAME"
password_hash = pylast.md5("YOUR_PASSWORD")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

user = pylast.User(user_name=username, network=network)

data = user.get_recent_tracks(limit=None)

def get_tags_names(data_point):
    tags = ""
    try:
        for d in data_point.track.artist.get_top_tags():
            tags = tags + d.item.name + ","
    except:
        tags = "N/A"
    return tags

df = pd.DataFrame(columns = ["timestamp", "playback_date", "title", "artist", "album", "tags"])

for i in range(len(data)):
    df.loc[i] = [data[i].timestamp, data[i].playback_date, data[i].track.title, data[i].track.artist.name, data[i].album, get_tags_names(data[i])]
    
    if i % 100 == 0:
        print (i)

df.to_csv("lastfmdata_tagged.csv", sep=",")

