from database import run,get 
from music_data import artists, albums, songs,cross_table
# CREATE TABLES 
# Artists: id, name, descrip
run (''' CREATE TABLE IF NOT EXISTS artists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING NOT NULL,
    description STRING NOT NULL    
    ) ''')

# Albums : id, name, discrip, genre
run ('''CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    al_title STRING NOT NULL,
    al_description STRING NOT NULL,
    year_released INTEGER, 
    genre STRING 
    ) ''')

# Songs: id, name, durations, URL 
run ('''CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    s_title STRING NOT NULL,
    duration STRING NOT NULL,
    v_id STRING   
    )''')

# ArtistXSongX Album: artist_id, song_id, album_id
run ('''CREATE TABLE IF NOT EXISTS artistsXsongsXalbums (
    artist_id INTEGER,
    album_id INTEGER,
    song_id INTEGER, 
    FOREIGN KEY (artist_id) REFERENCES artists (id),
    FOREIGN KEY (album_id) REFERENCES albums (id),
    FOREIGN KEY (song_id) REFERENCES songs (id)
    )''')

#INSERT datas to databas
#Artist 
# for artist in artists:
#  run ('INSERT INTO artists VALUES (NULL, :name, :description)', artists)

# Albums 
# for album in albums:
#     run ('INSERT INTO albums VALUES (NULL, :al_title, :al_description, :year_released, :genre)', albums)

#songs 
# for song in songs: 
#     run ('INSERT INTO songs VALUES (NULL, :s_title, :duration, :v_id)', songs)

#cross table
# for data in cross_table:
#     run ('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_table)

# Search Menu in Terminal 
#Print our all artist name
# allartist_names = get ('SELECT name FROM artists')
# print(allartist_names)
# #Print out oldest album
# oldest_albums = get ('''SELECT al_name 
#                         FROM albums
#                         WHERE (SELECT MIN(year_released) FROM albums)''')
# print(oldest_albums)
# #Uppdate albums without year_released with some year

#Adding data: add an artist 

#Adding data: add an album to artist
#Adding data : add a song to album
#Deliting data: delete an artist
#Deliting data: delete an album
#Deliting data: delete an album
#Average duration of songs
#Show the longest song from each album
#Number of songs each artist has 
#Search artist 
#Search songs    
