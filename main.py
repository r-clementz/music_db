from database import run,get,run_many
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
# run_many('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_table)

# Search Menu in Terminal 

#Print our all artist name
# allartist_names = get ('SELECT name FROM artists')
# print(allartist_names)

#Print out oldest album
# oldest_albums = get ('''SELECT al_title, year_released
#                         FROM albums 
#                         WHERE year_released = (SELECT MIN(year_released) FROM albums) 
#                     ''')
#print (oldest_albums)   

#Uppdate albums without year_released with some year
#get albums has no year_released
# albums_w_no_date = get ('''SELECT al_title, year_released 
#                             FROM albums 
#                             WHERE  year_released is NULL
#                         ''')
# #Show the album without released year and make user choose??                        
# #adding data to NULL year_released
# updated_year = input (int('Add released year:'))
# run ('''UPDATE albums
#         SET year_released = :year_released
#         WHERE year_released is NULL''',
#         {'year_rekeased':f'%{updated_year}%'}
#     )
                        
#Adding data: add an artist
# new_name = input('Please input new artist name: ')
# new_description = input('Please input description for the artist')

# new_artist = {'name': new_name,
#             'description': new_description}

# run ('INSERT INTO artists VALUES(NULL, :name, :desription)', new_artist )

#Adding data: add an album to artist
# picked_artist = get 
#Adding data : add a song to album
#Deliting data: delete an artist
# deliting_artist = input()
# run('''DELETE FROM artists WHERE name LIKE '%:name%' ''', {'name:': f'%{deliting_artist}%'})

#Deliting data: delete an album
# deliting_album = input()
# run('''DELETE FROM albums WHERE name LIKE '%:al_title%' ''', {'al_title:': f'%{deliting_artist}%'})

#Deliting data : song
# deliting_song = input()
#run('''DELETE FROM albums WHERE name LIKE '%:s_title%' ''', {'s_title:': f'%{deliting_song}%'})

#Average duration of all songs
#average_duration = run('SELECT ROUND(AVG(duration),2) AS Average_duration FROM songs')

#Average duration of each album
##get album name and id to check the duration


'''SELECT ROUND (AVG(duration),2)
FROM(SELECT * 
FROM songs 
JOIN artistsXsongsXalbums as cross
ON song_id
WHERE cross.song_id = songs.id and cross.album_id = 1)'''

#Show the longest song from each album
'''SELECT s_title, MAX(duration)
FROM(SELECT * 
FROM songs 
JOIN artistsXsongsXalbums as cross
ON song_id
WHERE cross.song_id = songs.id and cross.album_id = 1)
'''
#Number of songs each albums has
'''SELECT COUNT(album_id)
FROM(SELECT * 
FROM songs 
JOIN artistsXsongsXalbums as cross
ON song_id
WHERE cross.song_id = songs.id and cross.album_id = 1)'''

#Number of songs each artist has 
#get artist name and id 
artist_id = get('''SELECT artist_id 
FROM artistsXsongsXalbums
JOIN artists
ON id 
WHERE artist_id = artists.id 
AND artists.name LIKE '%:search_artist%'
GROUP BY artist_id''',f'%{search_artist}%')

'''SELECT COUNT(song_id)
FROM(SELECT * 
FROM artistsXsongsXalbums as cross
JOIN artists
ON id
WHERE cross.artist_id = artists.id and cross.artist_id = 1)'''

#Search artist 
'''
search_name = input()
get('SELECT name FROM artist WHERE name LIKE :search_name', {'name':f'%{search_name}}%')
'''

#Search songs 
'''search_song = input() 
get('SELECT s_title FROM songs WHERE s_title LIKE :search_name', {'name':f'%{search_name}}%')
'''

#all albums of artist
'''SELECT al_title
FROM albums
JOIN artistsXsongsXalbums as cross
ON album_id
WHERE cross.album_id = albums.id
AND cross.artist_id = 1
GROUP BY al_title'''
# Showing artist details together with all albums from that artist 
'''
SELECT al_title, ar.description, ar.name
FROM albums, artists AS ar 
JOIN artistsXsongsXalbums as cross
ON album_id
WHERE cross.album_id = albums.id
AND cross.artist_id = 1
GROUP BY al_title
'''

#Showing album detail and albums 
'''
SELECT al_title, al_description, name
FROM albums, artists 
JOIN artistsXsongsXalbums as cross
ON album_id
WHERE cross.album_id = albums.id
AND cross.artist_id = 1
GROUP BY al_title
'''


#Showing album details together with songs in that album 
#The list of total number of songs in the album and total playing time 

#Gör så att alla listor går att sortera på olika egenskaper, som name, year_released eller duration 
