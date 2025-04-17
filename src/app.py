import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "4AbDWrmJPSOeIbT2Ou60ik"

# Get the top tracks of an artist
results = spotify.artist_top_tracks(artist_id)

songs = []
for track in results['tracks']:
    songs.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': track['duration_ms'] / 60000
    })
    import pandas as pd
tracks_df = pd.DataFrame(songs)

print(tracks_df.head(5))

songs=[]
popularity=[]
duration=[]

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    songs.append(track['name'])
    popularity.append(track['popularity'])
    duration.append(track['duration_ms']/(1000*60)%60)

df = pd.DataFrame()

df['songs'] = songs
df['popularity'] = popularity
df['duration'] = duration

df_ascendente = df.sort_values(by='popularity', ascending=False)
 Popularity_duration_tracks = df.plot.scatter(x='duration',
                      y='popularity',
                      c='Red'
                      )
