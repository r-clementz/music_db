import json
from database import *
from query_helper import *

    
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





