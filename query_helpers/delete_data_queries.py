import json
from query_helper import *


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

