from database import*
from query_helper import *


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
