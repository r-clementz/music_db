from database import run,get,run_many,get_id
from music_data import artists, albums, songs,cross_table
from query_helper import *
import json


# create_artists_table()
# for artist in artists:
#     run_many('INSERT INTO artists VALUES (NULL, :name, :description)', artists)

create_albums_table()
# for album in albums:
#       run_many('INSERT INTO albums VALUES (NULL, :al_title, :al_description, :year_released, :genre)', albums)

create_songs_table()
# for song in songs: 
    # run_many('TINSERT INTO songs VALUES (NULL, :s_title, :duration, :v_id)', songs)

create_cross_table()
# for cross_info in cross_table:
#    run('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_info) 


'''
artist = input('Artist: ')
row_id = get("SELECT id FROM artists WHERE name = :search_name ", {'search_name': f'{artist}'})
id_dict =[dict(row_data) for row_data in row_id ]
json_id =json.dumps(id_dict)
print(json_id)
py_id = json.loads(json_id)
artist_id = py_id[0]["id"]      
print(artist_id)
'''
add_album()