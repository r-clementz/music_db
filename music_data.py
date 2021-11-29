import json
#Aritsts data: artists
artists =[
{'name': 'Robert Glasper',
 'description':"""Jazz pianist from Houston. 
  His pieces are influenced by a lot of different genres."""
},
{'name':'MF DOOM',
 'description':'Just remember ALL CAPS when you spell the man name. DOOM'
},
{'name':'Ryo Fukui',
 'description':'Jazz Pianist based in Sapporo (1948-2016)'}
]

#Albums data :albums
albums = [
{'al_title':'Black Radio',
 'al_description':'Best R&B Album at 55th Grammy Awards. Collab album with Shafiq Husayn, Eryka Babu, Lalah Hathaway, Lupe Fiasco, Bilal, Ledisi, We Are KING, Musiq Soulchild, Chrisette Michele,Meshell Ndegeocello, Stokley amd Yasiin Bey.',
 'year_released': 2012,
 'genre':'R&B'},
{'al_title':'ArtScience',
 'al_description':'Second Album released as Robert Glasper Experience ',
 'year_released': None,
 'genre':'Jazz'},
{'al_title':'Covered',
 'al_description':'',
 'year_released':2015,
 'genre':'Jazz'},
{'al_title':'THE MOUSE & THE MASK',
 'al_description':'',
 'year_released':2005,
 'genre':'Hiphop'},
{'al_title':'MM...FOOD',
 'al_description':'',
 'year_released':2004,
 'genre':'Hiphop'},
{'al_title':'Madvillainy',
 'al_description':'',
 'year_released':2004,
 'genre':'Hiphop'},
{'al_title':'Scenery',
 'al_description':'',
 'year_released':1976,
 'genre':'Jazz'},
{'al_title':'A Letter from Slowboat',
 'al_description':'',
 'year_released':2016,
 'genre':'Jazz'},
{'al_title':'Mellow Dream',
 'al_description':'',
 'year_released': None,
 'genre':'Jazz'}]

#songs data : songs 
songs =[]
with open ('songs.txt','r') as song_file:
    songs_json = song_file.read()
    imported_songs = json.loads(songs_json)

def convert_duration(song):
 """
  convert duration with 'mm:ss' format
  to seconds
 """
 duration = song['duration']
 m,s = duration.split(':')
 return int(m)*60 + int(s)

# convert durations to 'mm:ss' to seconds with funtiction
for song in imported_songs:
    converted_duration = convert_duration(song)
    converted_song = {
        's_title':song['s_title'],
        'duration':converted_duration, 
        'v_id' : song['v_id']
    }
    songs.append(converted_song)

        

#cross table data
cross_table = []
#Making data for aritst X album X song cross table with for loop  
artist1 = []
for i in range(1,36):
    if i <= 12:
        cross_info  = {
        'artist_id' : 1,
        'album_id': 1, 
        'song_id': i
        }
        artist1.append(cross_info)
    elif i >= 13 and i <= 24:
        cross_info  = {
        'artist_id' : 1,
        'album_id': 2, 
        'song_id': i
        }
        artist1.append(cross_info)
    else:
        ross_info  = {
        'artist_id' : 1,
        'album_id': 3, 
        'song_id': i
        }
        artist1.append(cross_info)
cross_table.append(artist1)

artist2 = []
for i in range(37,88):
    if i <= 52:
        cross_info  = {
        'artist_id' : 2,
        'album_id': 4, 
        'song_id': i
        }
        artist1.append(cross_info)
    elif i>=53 and i <= 67:
        cross_info  = {
        'artist_id' : 2,
        'album_id': 5, 
        'song_id': i
        }
        artist1.append(cross_info)
    else:
        ross_info  = {
        'artist_id' : 2,
        'album_id': 6, 
        'song_id': i
        }
        artist1.append(cross_info)
cross_table.append(artist2)  

artist3 = []
for i in range(89,108):
    if i <= 94:
        cross_info  = {
        'artist_id' : 3,
        'album_id': 7, 
        'song_id': i
        }
        artist1.append(cross_info)
    elif i >= 95 and i <= 102:
        cross_info  = {
        'artist_id' : 3,
        'album_id': 8, 
        'song_id': i
        }
        artist1.append(cross_info)
    else:
        ross_info  = {
        'artist_id' : 3,
        'album_id': 9, 
        'song_id': i
        }
        artist1.append(cross_info)
cross_table.append(artist3)    
