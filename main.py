from yandex_music import Client
import random

TOKEN = '...'
client = Client(TOKEN).init()
likes = client.users_likes_tracks().tracks_ids
random.shuffle(likes)
five_tracks = client.tracks(likes)
text = ''
for track in five_tracks[0:20]:
    name = track.title
    artist_list = track.artists_name()
    artist = ''
    for art in artist_list:
        artist += f'{art} '
    text += f'!play {artist}- {name}\n'
with open('track.txt', 'w', encoding='utf-8') as file:
    file.write(text)
