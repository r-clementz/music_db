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

'''INSERT INTO artistsXsongsXalbums
 VALUES ((SELECT id FROM artists WHERE name LIKE '%TEST%'), 2,3)'''
# artist_id = int(input('Artist_id:'))
# found_albums = get('''SELECT al_title
#                               FROM albums
#                               JOIN artistsXsongsXalbums as cross
#                               ON cross.album_id = albums.id
#                               WHERE cross.artist_id = :artist_id
#                               GROUP BY al_title''',
#                               {'artist_id':artist_id})
                              
# album_dict = [dict(found_album) for found_album in found_albums]                      
# jsonised_albums = json.dumps(album_dict)  
# all_albums_py = json.loads(jsonised_albums)                    
# for i in range (len(all_albums_py)):  
"""                
album = input('Album Title: ')
album_id = {"id": get_album_id(album)}
print (album_id['id'])
row_average= get('''SELECT ROUND (AVG(duration),2) AS avg_of_song_duration
                                 FROM (SELECT * 
                                    FROM songs 
                                    JOIN artistsXsongsXalbums as cross
                                    ON cross.song_id = songs.id 
                                    WHERE cross.album_id = :id )''', album_id)
average_dict =[dict(average) for average in row_average]
json_average= json.dumps(average_dict)
average_duration = json.loads(json_average)
print(f"The average song duration in this album : {average_duration[0]['avg_of_song_duration']}") """

album = {"al_title" : input('Album Title: ')}
album_id = {"id": get_album_id(album['al_title'])}
row_longest = get ('''SELECT s_title, MAX(duration)
                          FROM(SELECT * 
                               FROM songs 
                               JOIN artistsXsongsXalbums as cross
                               ON cross.song_id = songs.id
                               WHERE cross.album_id = :id )''', album_id)
longest_dict =[dict(song) for song in row_longest]
json_longest= json.dumps(longest_dict)
longest_song = json.loads(json_longest)

print(f"The average song duration in this album : {longest_song[0]['s_title']}, {longest_song[0]['MAX(duration)']}")                      
                        