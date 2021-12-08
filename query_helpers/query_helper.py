from os import get_exec_path
from database import run, get, run_many,get_id
from music_data import *

def create_artists_table():
    run (''' CREATE TABLE IF NOT EXISTS artists(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name STRING NOT NULL,
             description STRING ) ''')

def create_albums_table():
    run ('''CREATE TABLE IF NOT EXISTS albums(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            al_title STRING NOT NULL,
            al_description STRING,
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

        
def get_artist_id(artist):#
    '''
        Help function to get id from artists table
        to add id to artistsXsongsXalbums cross table.
        Search id by name which user input. 
        :param artist String 
    ''' 
    row_id = get("SELECT id, name FROM artists WHERE name LIKE :search_name ", {'search_name': f'%{artist}%'})
    id_dict =[dict(row_data) for row_data in row_id ]
    json_id =json.dumps(id_dict)
    py_id = json.loads(json_id)

    if len(py_id) > 1: 
        print("[id] / [Aritst name]")
        for i in range(len(py_id)):
            print(f"{py_id[i]['id']}\t{py_id[i]['name']}")
        artist_id = int(input("Please choose id for relevant artist"))    

    else:       
        artist_id = py_id[0]["id"]  
    
    return artist_id
   
def create_aritst_id(artist):
    artist_id = run('INSERT INTO artists (name) VALUES (:name)',{'name':f'{artist}'})
    print(artist," didn't exist in the database and added as new artist")
    print(f"id for {artist}: {artist_id}") 
    #return artist_id

# Albums 

def get_album_id(album):##
        row_id = get("SELECT id, al_title FROM albums WHERE al_title LIKE :search_name ", {'search_name': f'%{album}%'})
        id_dict =[dict(row_data) for row_data in row_id ]
        json_id =json.dumps(id_dict)
        py_id = json.loads(json_id)
        
        if len(py_id) > 1: 
            print("[id] / [Album title]")
            for i in range(len(py_id)):
                print(f"{py_id[i]['id']}\t{py_id[i]['al_title']}")
            album_id = int(input("Please choose id for relevant album"))    

        else:       
            album_id= py_id[0]["id"] 
          
  
        return album_id

  
def create_album_id(album):#            
    album_id = run('INSERT INTO albums (al_title) VALUES (:al_title)',{'al_title':f'{album}'})
    print("The album was added and the id for this album was also created")
   #print(f"id for {album}: {album_id}")   
    return album_id


#songs 

#ID 
def get_song_id(song):##
        row_id = get("SELECT id, s_title FROM songs WHERE s_title LIKE :search_name ", {'search_name': f'%{song}%'})
        id_dict =[dict(row_data) for row_data in row_id ]
        json_id =json.dumps(id_dict)
        print(json_id) 
        py_id = json.loads(json_id)

        if len(py_id) > 1: 
            print("[id] / [Song title]")
            for i in range(len(py_id)):
                print(f"{py_id[i]['id']}\t{py_id[i]['s_title']}")
            song_id = int(input("Please choose id for relevant song"))    
        else:       
            song_id= py_id[0]["id"] 
        
        return song_id

  
def create_album_id(song):#            
    song_id = run('INSERT INTO songs (s_title) VALUES (:s_title)',{'s_title':f'{song}'})
    print("The song was added and the id for this album was also created")
    print(f"id for {song}: {song_id}")   
    return song_id



