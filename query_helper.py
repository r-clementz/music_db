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




#QUERIES
#Adding Artist 
def add_artist():#
    name = input('Artist Name:')
    description = input ('Artist Description: ')
    artist_id = (run('INSERT INTO artists VALUES (NULL, ?, ?)',(name, description)))
    new_artist = {
        'id' : artist_id,
        'name': f'%{name}%',
        'description': f'%{description}%'
    }
    print(artist_id)
    run('INSERT INTO artistsXsongsXalbums (artist_id) VALUES (:id)', new_artist)
    print ('artist_id was created in cross table')

        

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
def add_album ():#
    artist = input('Artist : ')
    title = input('Album Title:')
    description = input('Album Description:')
    year_released  = int(input('Released Year (YYYY)):'))
    genre = input('Album Genre: ')
    new_album = {'artist' : artist,
                 'al_title' : title,
                 'al_description' : description,
                 'year_released' : year_released,
                 'genre' : genre}

    album_id = run('''INSERT INTO albums 
                        VALUES (NULL, :al_title, :al_description, :year_released, :genre)''', 
                        new_album)                        
    print ('The album added to albums table','\nalbum_id: ',album_id )
    #Get artist id 
    try: 
        artist_id = get_artist_id(title)
    except:
        artist_id = create_aritst_id(title) 

    cross_data = {'artist_id': artist_id,
                  'album_id' : album_id}       

    run('INSERT INTO  artistsXsongsXalbums (artist_id, album_id) VALUES (:artist_id, :album_id)', cross_data)
    print("Album's information added to cross table")

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
def add_song():#
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
    for new_song in new_songs:                
         song_id = (run('INSERT INTO songs (s_title, duration) VALUES (?, ?)', (title, converted_duration)))
         song_id_list.append(song_id)
    #get artist id 
    try:
        artist_id = get_artist_id(artist)
    except:
        artist_id = create_aritst_id(artist) 
    #get album_id
    try:
        album_id = get_album_id(album)
    except:       
        album_id = create_album_id(album)
    #Add and update cross table data  
    cross_data=[]    
    for song_id in song_id_list:
        cross_ids= {
        'artist_id' : artist_id,
        'album_id': album_id, 
        'song_id': song_id
       }
        cross_data.append(cross_ids)
    
    for cross_id in cross_data:
        run('INSERT INTO artistsXsongsXalbums VALUES (:artist_id, :album_id, :song_id )',cross_id)
        print('artist_id: ',cross_id['artist_id'], 
              'album_id:', cross_id['album_id'], 
              'song_id :', cross_id['song_id'], 
              'added to artistsXsongsXalbums')
    print('All new songs added to cross table')  

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

    
def print_all_artists():#
    '''
        Print all aritsts name in artists table
    '''
    row_artists= get ('SELECT name FROM artists')
    artists_dict = [dict(row_artist) for row_artist in row_artists]
    jsonised_artists = json.dumps(artists_dict)
    all_artists = json.loads(jsonised_artists)
    for artist in all_artists:
     print(artist['name'])

def print_all_albums():  
    row_albums= get ('SELECT al_title FROM albums')
    albums_dict = [dict(album) for album in row_albums]
    jsonised_albums = json.dumps(albums_dict)
    all_albums = json.loads(jsonised_albums)
    for album in all_albums:
     print(album['al_title'])

def print_all_songs():
    row_songs= get ('SELECT s_title FROM songs')
    songs_dict = [dict(song) for song in row_songs]
    jsonised_songs = json.dumps(songs_dict)
    all_songs = json.loads(jsonised_songs)
    for song in all_songs:
     print(song['s_title'])
    pass


def print_oldest_album():#
    '''
        Print out oldest album in albums 
    '''    
    row_oldest_albums = get ('''SELECT al_title, year_released
                        FROM albums 
                        WHERE year_released = (SELECT MIN(year_released) FROM albums) 
                     ''')
    oldest_als_dict = [dict(row_oldest_al) for row_oldest_al in row_oldest_albums]
    jsonised_albums = json.dumps(oldest_als_dict)
    oldest_albums = json.loads(jsonised_albums)
    for album in oldest_albums:
        print(album['al_title'])                 
     

def update_released_year():#
    '''
        Uppdate year_released with the year user input
        if it is null.
    '''                                        
#get albums with no released year
    try:
        row_albums_wo_year = get('SELECT id, al_title FROM albums WHERE year_released is NULL')
        woy_album_dict = [dict(album) for album in row_albums_wo_year ]
        jsonised_albums = json.dumps(woy_album_dict)
        albums_wo_year = json.loads(jsonised_albums)
        for album in albums_wo_year:
            print(f"id {album['id']} : {album['al_title']}")
    except: 
        print("Couldn't find any album withour released year")  

#user choose album id to add year 
    chosen_al_id = int(input("Please choose one id you'd like to add released year: ")) 
    updated_year = int (input('Add released year:')) 
    inputs ={"year_released":updated_year,
                     "id": chosen_al_id}              
#adding year_released to chosen album 
    try:                 
        run('''UPDATE albums
            SET year_released = :year_released
            WHERE id = :id''',inputs)
        print (f"The released year for album({chosen_al_id}) is updated")    
    except: 
        print(":( We got an error and couldn't change released year")        

def delete_artist():#
    '''
        Delete an artist from database
    '''    
    try:
        deleting_artist = {'name': input("Artist you'd like to delete :")}
        
        run("DELETE FROM artists WHERE name LIKE :name ", deleting_artist)
        print(delete_artist['name']," was deleted.")
    except:
        print(deleting_artist['name']," doesn't exist in the database")   

def delete_album():#
    '''
        Delete an album from database
    '''
    try:
        deliting_album = { 'al_title' : input("Album you'd like to delete: ")}
        al_id = {"id":get_album_id(deliting_album['al_title'])}
        #Delete album from albums table 
        run("DELETE FROM albums WHERE al_title LIKE :al_title ", deliting_album)
        print(deliting_album['al_title']," was deleted from albums")
        #Delete album_id from cross table 
        run("DELETE FROM artistsXsongsXalbums WHERE album_id = :id", al_id)
        print("The album was also deleted from artistsXsongsXalbums")
     
    except:
         print(deliting_album["al_title"]," doesn't exist in the database")    

def delete_song():#
    '''
        Delete a song from database
    '''
    try:
        deliting_song =  input("Song you'd like to delete:")
        s_id = get_song_id(deliting_song)
        run("DELETE FROM songs WHERE s_title LIKE :s_title ", {'s_title': f"%{deliting_song}%" })
        print(deliting_song," was deleted from songs")
        run("DELETE FROM artistsXsongsXalbums WHERE song_id = :id" , s_id)
        print ("The song was also deleted from artistsXsongsXalbums")
    except:
         print(deliting_song['s_title']," doesn't exist in the database")    

    
def get_average_duration_of_songs():#
    '''
        Get and print the average duration of all songs
    '''
    row_average = get('SELECT ROUND(AVG(duration),2) AS average_duration FROM songs')
    average_dict = [dict(average) for average in row_average]
    json_average = json.dumps(average_dict)
    average_duration = json.loads (json_average)
    print(f"Average duration for all songs in this database: {average_duration[0]['average_duration']}")

#Average duration of each album
##get album name and id to check the duration

def get_average_song_duration_in_album(album):#
    '''
        Get and print the average duration of songs
        in an album chosen by user  
    '''
    try:
        album_id = {"id": get_album_id(album)}
        row_average= get('''SELECT ROUND (AVG(duration),2) AS avg_of_song_duration
                                 FROM (SELECT * 
                                    FROM songs 
                                    JOIN artistsXsongsXalbums as cross
                                    ON cross.song_id = songs.id 
                                    WHERE cross.album_id = :id )''', album_id)
        average_dict =[dict(average) for average in row_average]
        json_average= json.dumps(average_dict)
        average_duration = json.loads(json_average)
        print(f"""The average song duration in this album : 
                {average_duration[0]['avg_of_song_duration']}""")
    except:  
         print("Couldn't get any data.")                

def get_longest_song_in_album(title):#
    '''
        Get and print the longest song in an album
        chosesen by user
    '''
    try:
        album = {"al_title" : title }
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
        print(f"The longest song in this album : {longest_song[0]['s_title']}, {longest_song[0]['MAX(duration)']}")                      
                        
    except:
        print(album," doesn't exist in the database")

def get_number_of_songs_in_albums(album):#
    '''
        Get then number of songs in albums user chose.
    '''
    try:
        album = {"al_title" : album}
        album_id = { "id": get_album_id(album['al_title'])}
        row_number =get('''SELECT COUNT(album_id)
                             FROM(SELECT * 
                                  FROM songs 
                                  JOIN artistsXsongsXalbums as cross
                                  ON cross.song_id = songs.id 
                                  WHERE cross.album_id = :id)''',album_id)
        number_dict =[dict(row) for row in row_number]
        json_number = json.dumps(number_dict)
        number_of_songs = json.loads(json_number)                          
        print(f"{number_of_songs[0]['COUNT(album_id)']} songs in the album")
    except:
        print(album," doesn't exist in the database")



def search_artist(search_name):#
    '''
        Search an aritst in database by artist name 
        and print the result.
    '''
    #search_name =  input('Name or Keyword to search an artist: ')
    try:
        row_found_artist = get('SELECT id, name FROM artists WHERE name LIKE :name',{'name':f'%{search_name}%' })
        artist_dict = [dict(artist) for artist in row_found_artist]
        json_artist = json.dumps(artist_dict)
        found_artist = json.loads(json_artist)
        print('Search Result:\n (id) / name')
        for i in range(len(found_artist)):
            print(f"({found_artist[i]['id']})  {found_artist[i]['name']}")
        return True     
    except:
        print ("Couldn't find any artist with ", search_name)    
        return False 
    
def search_song(song):#
    '''
        Search a song by name or key word 
        and print the result.
    '''
    try:
        row_found_songs = get('SELECT id, s_title FROM songs WHERE s_title LIKE :s_title',{'s_title':f'%{song}%' })
        song_dict = [dict(song) for song in row_found_songs]
        json_song = json.dumps(song_dict)
        found_song = json.loads(json_song)
       
        print('Search Result:\n (id) / title')
        for i in range(len(found_song)):
            print(f"({found_song[i]['id']})  {found_song[i]['s_title']}")
        return True
    except:
        print ("Couldn't find any song like ", song)    
        return False
def search_song_w_artist(song):
    '''
        Search a song by title or key word.
        The reult will be shown together with the artist name. 
    '''
    #'Name or Keyword to search a song
    try:
        row_found_songs = get('''SELECT songs.id, s_title, artists.name
                                 FROM songs, artists
                                 JOIN artistsXsongsXalbums as cross
                                 ON artists.id = cross.artist_id 
                                 AND songs.id = song_id
                                 WHERE songs.s_title LIKE  :s_title''',
                                 {'s_title':f'%{song}%' })                         
        song_dict = [dict(song) for song in row_found_songs]
        json_song = json.dumps(song_dict)
        found_song = json.loads(json_song)
       
        print('Search Result:\n [id] / [title] /[artist]')
        for i in range(len(found_song)):
            print(f"({found_song[i]['id']})\t{found_song[i]['s_title']}\t/ {found_song[i]['name']}")

    except:
        print ("Couldn't find any song like ", song)   

def search_album(album):
    try:
        row_found_album = get('SELECT id, al_title FROM albums WHERE al_title LIKE :al_title',{'s_title':f'%{album}%' })
        album_dict = [dict(song) for song in row_found_album]
        json_album = json.dumps(album_dict)
        found_album = json.loads(json_album)
       
        print('Search Result:\n (id) / title')
        for i in range(len(found_album)):
            print(f"({found_album[i]['id']})  {found_album[i]['al_title']}")
        return True
    except:
        print ("Couldn't find any album like ", album)    
        return False         
    
def all_albums_of_artist(artist):#
    '''
        Seach all albums of an aritst which user input 
    '''
    artist_id = get_artist_id(artist) 
  
    try: 
        found_albums = get('''SELECT id, al_title
                              FROM albums
                              JOIN artistsXsongsXalbums as cross
                              ON cross.album_id = albums.id
                              WHERE cross.artist_id = :artist_id
                              GROUP BY al_title''',
                              {'artist_id':artist_id})

        album_dict = [dict(found_album) for found_album in found_albums]                      
        jsonised_albums = json.dumps(album_dict)  
        all_albums_py = json.loads(jsonised_albums)
        
        print('Search Result:\n (id) / title')
        for i in range (len(all_albums_py)):                    
            print(f"{all_albums_py[i]['id']}  {all_albums_py[i]['al_title']}")
    except:
        print(":( Couldnt't find any album info of ",artist)                              

def get_album_list_w_details(artist):#
    '''
        Get and print the album details and albums 
        of the artist which user chosen
    '''
    artist_id = get_artist_id(artist) 
   
    try: 
        row_info = get('''SELECT id, al_title, al_description
                              FROM albums
                              JOIN artistsXsongsXalbums as cross
                              ON cross.album_id = albums.id
                              WHERE cross.artist_id = :artist_id
                              GROUP BY al_title''',
                              {'artist_id':artist_id})
        album_dict =[dict(info) for info in row_info]    
        jsonised_info = json.dumps(album_dict)
        found_albums = json.loads(jsonised_info)  
        print('Search Result:\n (id) / title / info')             
        for i in range(len(found_albums)):
            print(f"{found_albums[i]['id']}  {found_albums[i]['al_title']} : {found_albums[i]['al_description']}")
            
    except:
        print("Couldnt't find any info of ",artist)         

def get_all_songs_in_albums_w_details(artist):#
    '''
        Get and print all songs in the album of the artist 
        which user chosen. Album details also shown.
    '''
    try: 
        row_info = get('''SELECT songs.id, s_title , al_title, al_description
                                            FROM songs,albums
                                            JOIN artistsXsongsXalbums AS cross
                                            ON cross.album_id = albums.id 
                                            AND cross.song_id = songs.id
                                            WHERE cross.artist_id = (SELECT artists.id 
                                                                     FROM  artistsXsongsXalbums
                                                                     JOIN artists
                                                                     ON cross.artist_id = artists.id  
                                                                     WHERE artists.name LIKE :name)''',
                                            {'name':f'%{artist}%'} )
        album_dict =[dict(info) for info in row_info]    
        jsonised_info = json.dumps(album_dict)
        found_albums = json.loads(jsonised_info)  
        print('Search Result:\n id / song \t/ album / info')             
        for i in range(len(found_albums)):
             print(f"{found_albums[i]['id']}\t{found_albums[i]['s_title']}\t{found_albums[i]['al_title']}: {found_albums[i]['al_description']}")
                                                                    
    except:
        print("Couldnt't find any info of ",artist)                                                               

def get_nr_of_songs_and_total_durations(album):#
    '''
        Get and print the list of total number of songs 
        in the album and total playing time 
    '''
    try: 
        row_info = get('''SELECT al_title, COUNT(song_id),SUM(duration) 
                                      FROM songs, albums
                                      JOIN artistsXsongsXalbums as cross
                                      ON song_id = songs.id
                                      WHERE cross.album_id = albums.id 
                                      AND cross.song_id = songs.id
                                      AND cross.album_id = (SELECT id 
                                                            FROM albums 
                                                            WHERE albums.al_title LIKE :al_title ) ''',
                                      {'al_title':f'%{album}%'})

        info_dict =[dict(info) for info in row_info]    
        jsonised_info = json.dumps(info_dict)
        found_info = json.loads(jsonised_info)  
        #If there's album but no information
        if found_info[0]['al_title'] == None  or found_info[0]['COUNT(song_id)'] ==0:
            print ("Couldnt't find any info of ",album) 
        
        print('Search Result:\n Album / Number of songs / duration (seconds)')             
        for i in range(len(found_info)):
             print(f"{found_info[i]['al_title']}\t{found_info[i]['COUNT(song_id)']}\t({found_info[i]['SUM(duration)']})")
    except:                                                     
          print("Couldnt't find ",album) 

def print_longest_album():
    row_album = get('''SELECT artists.name, al_title, MAX(total_duration)
                       FROM artists,(SELECT al_title, SUM(duration) AS total_duration FROM songs, albums
                            JOIN artistsXsongsXalbums as cross
                            ON cross.song_id = songs.id
                            WHERE cross.album_id = albums.id 
                            AND cross.song_id = songs.id
                            AND cross.album_id < (SELECT COUNT(albums.id) FROM albums) 
                            GROUP BY al_title)''')
    album_dict = [dict(album) for album in row_album]
    json_album = json.dumps(album_dict)
    print(json_album) 
    py_album =json.loads(json_album)
    for i in range(len(py_album)):
        print(f"The Longest Album is {py_album[i]['al_title']} of {py_album[i]['name']}\t(total {py_album[i]['MAX(total_duration)']} seconds) ")





