from yandex_music import Client
import random

TOKEN = '...'
count = 5
shufle = True

client = Client(TOKEN).init()
likes = client.users_likes_tracks().tracks_ids
if shufle:
    random.shuffle(likes)
track_list = client.tracks(likes)
text = ''
for track in track_list[0:count]:
    name = track.title
    artist_list = track.artists_name()
    artist = ''
    for art in artist_list:
        artist += f'{art} '
    text += f'!play {artist}- {name}\n'
with open(f'track_list.txt', 'wt', encoding='utf_8') as file:
    file.write(text)

