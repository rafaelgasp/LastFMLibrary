import pylast
import pandas as pd

API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
username = "YOUR_USERNAME"
password_hash = pylast.md5("YOUR_PASSWORD")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

df = pd.read_csv("artistLastFM.csv", sep="\n")
df['tags'] = ""

def get_tags_artist(artist_name):
    artist_obj = network.get_artist(artist_name)
    tags = ""
    j = 0
    try:
        for d in artist_obj.get_top_tags():
            tags = tags + d.item.name + ","
            j = j + 1
            if j == 5: 
                break
    except:
        tags = "N/A"
    return tags[:len(tags)-1]

for i in range(0, len(df)):
    df['tags'][i] = get_tags_artist(df['artist'][i])
    
    if i % 100 == 0:
        print (i)
        
df.to_csv("lastfmdata_tagged.csv", sep=",")