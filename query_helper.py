from os import get_exec_path
from database import run, get, run_many,runs
from music_data import *

def create_artists_table():
    run (''' CREATE TABLE IF NOT EXISTS artists(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name STRING NOT NULL,
             description STRING NOT NULL) ''')

def create_albums_table():
    run ('''CREATE TABLE IF NOT EXISTS albums(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            al_title STRING NOT NULL,
            al_description STRING NOT NULL,
            year_released INTEGER, 
            genre STRING ) ''')

def create_songs_table():
    run ('''CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            s_title STRING NOT NULL,
            duration STRING NOT NULL,
            v_id STRING )''')

def create_cross_table():
    run ('''CREATE TABLE IF NOT EXISTS artistsXsongsXalbums (
            artist_id INTEGER,
            album_id INTEGER,
            song_id INTEGER, 
            FOREIGN KEY (artist_id) REFERENCES artists (id)
            ON DELETE CASCADE,
            FOREIGN KEY (album_id) REFERENCES albums (id)
            ON DELETE CASCADE,
            FOREIGN KEY (song_id) REFERENCES songs (id)
            ON DELETE CASCADE
            )''')


#INSERT DATA TO SQLite
#Artist 
'''
for artist in artists:
    run ('INSERT INTO artists VALUES (NULL, :name, :description)', artists)
'''
# Albums 
''' 
for album in albums:
     run ('INSERT INTO albums VALUES (NULL, :al_title, :al_description, :year_released, :genre)', albums)
'''
#songs 
'''
for song in songs: 
     run ('INSERT INTO songs VALUES (NULL, :s_title, :duration, :v_id)', songs)
'''
#cross table

""" for data in cross_table:
 run('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_table) """




#QUERIES
#Adding Artist 
def add_artist():
    name = input('Artist Name:')
    description = input ('Artist Description: ')
    artist_id =(run ('INSERT INTO artists VALUES (NULL, ?, ?)', (name,description)))
    print('The artist added to artists table' )
    new_artist = {
        'id' : artist_id,
        'name': name,
        'description': description
    }
    print(artist_id)
    run('INSERT INTO artistsXsongsXalbums (artist_id) VALUES (:id)', new_artist)
    print ('artist_id was created in cross table')
    
def get_artist_id(artist):
    '''
        Help function to get id from artists table
        to add id to artistsXsongsXalbums cross table.
        Search id by name which user input. 
        :param artist String 
    '''
    try: #check if the artist is already in data 
        artist_id = get ('SELECT id FROM artist WHERE name LIKE ?', (artist))
        return artist_id
    except: # if not, insert the artist to artists table and get id 
        artist_id = run ('INSERT INTO aritst (name) VALUES (?)', (artist))
        return artist_id

# Albums 
def add_album ():
    artist = input('Artist : ')
    title = input('Album Title:')
    description = input('Album Description:')
    year_released  = int(input('Released Year (YYYY)):'))
    genre = input('Album Genre: ')
    new_album = {'artist' : artist,
                 'al_title' : title,
                 'al_description' : description,
                 'year_released' : year_released,
                 'genre' : genre
        }
    album_id = (run ('''INSERT INTO albums 
                        VALUES (:al_title, :al_description, :year_released, :genre)''', 
                        new_album))                        
    print ('The album added to albums table','\nalbum_id: ',album_id )
    #Get artist id 
    cross_data = {'artist_id': get_artist_id(artist),
                  'album_id' : album_id}       

    run('INSERT INTO  artistsXsongsXalbums (artist_id, album_id) VALUES (:aritist, :id)', cross_data)
    print("Album's information added to cross table")

def get_album_id(album):
    try:
        album_id = get ('SELECT id FROM artist WHERE name LIKE ?', (album))
        return album_id    
    except:
        album_id = run ('INSERT INTO aritst (name) VALUES (?)', (album))
        return album_id    


#songs 
def add_song():
    artist = input('Artist : ')
    album = input ('Album Title: ')
    number_of_new_songs = int(input ("How many songs you'd like to add? :"))
    new_songs =[]
    
    #Get all info of songs to add 
    for new_song in range(number_of_new_songs):
        title = input('Song Title: ')
        duration = input('Song Duration (mm:ss):')
        converted_duration = duration_converter(duration)
        new_song = {'s_title': title,
                    'duration': converted_duration}
        new_songs.append(new_songs)
   
    #Add all songs in new song list and get song_id
    song_id_list=[]
    for song in new_songs:                
         song_id = (run('INSERT INTO songs (s_title, duration) VALUES (:s_title, :duration)', new_song))
         song_id_list.append(song_id)
    
    #get artist id 
    artist_id = get_artist_id(artist)
    #get album_id
    album_id = get_album_id(album)     
 
    #Add and update cross table data      
    for song_id in song_id_list:
        cross_info  = {
        'artist_id' : artist_id,
        'album_id': album_id, 
        'song_id': song_id
       }
        cross_table.append(cross_info)
    
    for cross_info in cross_table:
        run_many('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_info)
        print('artist_id: ',cross_info['artist_id'], 
              'album_id:', cross_info['album_id'], 
              'song_id :', cross_info['song_id'], 
              'added to artistsXsongsXalbums')
    print('All new songs added to cross table')    
    
def print_all_artists():
    '''
        Print all aritsts name in artists table
    '''
    all_artists= get ('SELECT name FROM artists')
    print(all_artists)

def print_oldest_album(): 
    '''
        Print out oldest album in albums 
    '''    
    oldest_albums = get ('''SELECT al_title, year_released
                        FROM albums 
                        WHERE year_released = (SELECT MIN(year_released) FROM albums) 
                     ''')
    print (oldest_albums)   

def update_released_year():
    '''
        Uppdate year_released with the year user input
        if it is null.
    '''                                        
#adding data to NULL year_released
    try:
        updated_year = input (int('Add released year:'))
        run ('''UPDATE albums
            SET year_released = :year_released
            WHERE year_released is NULL''',
            {'year_released':f'%{updated_year}%'})
    except: 
        print("Couldn't find any album withour released year")        

def delete_artist():
    '''
        Delete an artist from database
    '''    
    try:
        deliting_artist = input()
        run('''DELETE FROM artists WHERE name LIKE '%:name%' ''', {'name': f'%{deliting_artist}%'})
        print(delete_artist," was deleted.")
    except:
        print(delete_artist," doesn't exist in the database")   

def delete_album():
    '''
        Delete an album from database
    '''
    try:
        deliting_album = input()
        run('''DELETE FROM albums WHERE name LIKE '%:al_title%' ''', {'al_title': f'%{deliting_album}%'})
        print(deliting_album," was deleted.")
    except:
         print(deliting_album," doesn't exist in the database")    

def delete_song():
    '''
        Delete a song from database
    '''
    try:
        deliting_song = input()
        run('''DELETE FROM albums WHERE name LIKE '%:s_title%' ''', {'s_title': f'%{deliting_song}%'})
        print(deliting_song," was deleted.")
    except:
         print(deliting_song," doesn't exist in the database")    

    
def get_average_duration_of_songs():
    '''
        Get and print the average duration of all songs
    '''
    average_duration = get('SELECT ROUND(AVG(duration),2) AS Average_duration FROM songs')
    print(average_duration)

#Average duration of each album
##get album name and id to check the duration

def get_average_duration_in_album():
    '''
        Get and print the average duration of songs
        in an album chosen by user  
    '''
    try:
        album = input('Album Title: ')
        album_id = get_album_id(album)
        average_duration= get('''SELECT ROUND (AVG(duration),2)
                                 FROM (SELECT * 
                                    FROM songs 
                                    JOIN artistsXsongsXalbums as cross
                                    ON cross.song_id = songs.id 
                                    WHERE cross.album_id = :album_id )''',
                                {'album_id': f'%{album_id}%'})
        print(average_duration) 
    except:  
         print(album," doesn't exist in the database")                

def get_longest_song_in_album():
    '''
        Get and print the longest song in an album
        chosesen by user
    '''
    try:
        album = input('Album Title: ')
        album_id = get_album_id(album)
        longest_song = get ('''SELECT s_title, MAX(duration)
                          FROM(SELECT * 
                               FROM songs 
                               JOIN artistsXsongsXalbums as cross
                               ON cross.song_id = songs.id
                               WHERE cross.album_id = :album_id )''',
                        {'album_id': f'%{album_id}%'} )
        print (longest_song)                          
    except:
        print(album," doesn't exist in the database")

def get_number_of_songs_in_albums():
    '''
        Get then number of songs in albums user chose.
    '''
    try:
        album = input('Album Title: ')
        album_id = get_album_id(album)
        number_of_songs =('''SELECT COUNT(album_id)
                             FROM(SELECT * 
                                  FROM songs 
                                  JOIN artistsXsongsXalbums as cross
                                  ON cross.song_id = songs.id 
                                  WHERE cross.album_id = :album_id)''',
                            {'album_id':f'%{album_id}%'})
        print(number_of_songs)
    except:
        print(album," doesn't exist in the database")



def search_artist():
    '''
        Search an aritst in database by artist name 
        and print the result.
    '''
    search_name = input('Name or Keyword to search an artist: ')
    try:
        found_artist = get('SELECT name FROM artist WHERE name LIKE :search_name', {'name':f'%{search_name}%'})
        print(found_artist)
    except:
        print ("Couldn't find any artist with ", search_name)    

    
def search_song():
    '''
        Search a song by name or key word 
        and print the result.
    '''
    search_name = input('Name or Keyword to search a song: ')
    try:
        found_song = get('SELECT name FROM artist WHERE name LIKE :search_name', {'name':f'%{search_name}%'})
        print(found_song)
    except:
        print ("Couldn't find any artist with ", search_name)    

    
def all_albums_of_artist():
    '''
        Seach all albums of an aritst which user input 
    '''
    search_name = input("Artist you'd like to see all albums: ")
    artist_id = get_exec_path(search_name)
    try: 
        found_albums = get('''SELECT al_title
                              FROM albums
                              JOIN artistsXsongsXalbums as cross
                              ON cross.album_id = albums.id
                              WHERE cross.artist_id = :artist_id
                              GROUP BY al_title''',
                              {'artist_id':f'%{artist_id}%'})
        print(found_albums)
    except:
        print("Couldnt't find any info of ",search_name)                              

def get_album_details():
    '''
        Get and print the album details and albums 
        of the artist which user chosen
    '''
    search_name = input("Artist you'd like to see all albums: ")
    artist_id = get_exec_path(search_name)
    try: 
        found_albums = get('''SELECT al_title, al_description, name
                              FROM albums, artists 
                              JOIN artistsXsongsXalbums as cross
                              ON cross.album_id = albums.id
                              WHERE cross.artist_id = :artist_id
                              GROUP BY al_title''',
                              {'artist_id':f'%{artist_id}%'})
        print(found_albums)
    except:
        print("Couldnt't find any info of ",search_name)         

def get_all_songs_in_albums_w_details():
    '''
        Get and print all songs in the album of the artist 
        which user chosen. Album details also shown.
    '''
    search_name = input("Artist you'd like to see all albums: ")
    try: 
        found_songs_and_al_details = get('''SELECT s_title,al_title,al_description
                                            FROM songs,albums
                                            JOIN artistsXsongsXalbums AS cross
                                            ON cross.album_id = albums.id 
                                            AND cross.song_id = songs.id
                                            WHERE cross.artist_id = (SELECT artist_id 
                                                                     FROM  artistsXsongsXalbums
                                                                     JOIN artists
                                                                     ON cross.artist_id = artists.id  
                                                                     WHERE artists.name LIKE ?''',
                                            {'name':f'%{search_name}%'} )
        print(found_songs_and_al_details) 
    except:
        print("Couldnt't find any info of ",search_name)                                                               

def get_nr_of_songs_and_total_durations():
    '''
        Get and print the list of total number of songs 
        in the album and total playing time 
    '''
    search_name = input("Album you'd like to see all songs and duration: ")
    try: 
        total_songs_duration = get('''SELECT al_title, 
                                      COUNT(song_id) AS total_songs,
                                      SUM(duration) AS total_length
                                      FROM songs, albums
                                      JOIN artistsXsongsXalbums as cross
                                      ON song_id = songs.id
                                      WHERE cross.album_id = albums.id 
                                      AND cross.song_id = songs.id
                                      AND cross.album_id = (SELECT id 
                                                            FROM albums 
                                                            WHERE albums.al_title LIKE ?) ''',
                                      {'al_title':f'%{search_name}%'})
    except:                                                     
          print("Couldnt't find ",search_name) 


#Gör så att alla listor går att sortera på olika egenskaper, som name, year_released eller duration 
