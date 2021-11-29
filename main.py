from database import run,get 
from music_data import artists, albums, songs,cross_table
# CREATE TABLES 
# Artists: id, name, descrip
run (''' CREATE TABLE IF NOT EXISTS artists(
    id INTEGER PRIMARY KEY AUTOINCEREMENT,
    name STRING NOT NULL,
    description STRING NOT NULL    
    ) ''')

# Albums : id, name, discrip, genre
run ('''CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY AUTOINCEREMENT,
    al_title STRING NOT NULL,
    al_description STRING NOT NULL,
    year_released INTEGER NOT NULL, 
    genre STRING 
    ) ''')

# Songs: id, name, durations, URL 
run ('''CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCEREMENT,
    s_title STRING NOT NULL,
    duration STRING NOT NULL,
    v_id STRING   
    )''')

# ArtistXSongX Album: artist_id, song_id, album_id
run ('''CREATE TABLE IF NOT EXISTS artistsXsongsXalbums (
    artist_id INTEGER FOREIGNKEY artists(id),
    album_id INTEGER FOREIGN KEY albums(id),
    song_id INTEGER FOREIGN KEY songs(id)
    )''')

#INSERT datas to databas
#Artist 
for artist in artists:
 run ('INSERT INTO artists VAKUES (NULL, :name, :description)', artist)

# albums 
for album in albums:
    run ('INSERT INTO albums VALUES (NULL,:al_title, : year_released, :genre)', album)

#songs 
for song in songs: 
    run ('INSERT INTO songs VALUES (NULL, :s_title, :duration, :v_id)', song)

#cross table
for data in cross_table:
    run ('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',data)