from database import*
from query_helper import *



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
