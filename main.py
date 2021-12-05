from database import run,get,run_many
from music_data import artists, albums, songs,cross_table
from query_helper import *


create_artists_table()
# for artist in artists:
#     run ('INSERT INTO artists VALUES (NULL, :name, :description)', artists)

create_albums_table()
# for album in albums:
#      run_many('INSERT INTO albums VALUES (NULL, :al_title, :al_description, :year_released, :genre)', albums)

create_songs_table()
# for song in songs: 
#     run_many('INSERT INTO songs VALUES (NULL, :s_title, :duration, :v_id)', songs)

create_cross_table()
# for data in cross_table:
#  run_many('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_table) 

