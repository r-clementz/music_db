from database import run,get 
from music_data import artists, albums, cross_table
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
    song_id INTEGER FOREIGN KEY songs(id),
    album_id INTEGER FOREIGN KEY albums(id)
    )''')
