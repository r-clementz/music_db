from flask import Flask, jsonify,render_template,request,redirect
from database import run, get

app = Flask(__name__,static_folder = 'static', static_url_path="")

#TOP PAGE
@app.get("/")
def index():
    """
    """
    all_artists = get('SELECT * FROM aritst')
    all_artists = [dict(artist) for artist in all_artists]
    return jsonify(all_artists)
    

@app.get('/users')
def get_users():
 users = get('SELECT * FROM users')
 users = [dict(user) for user in users]
 return jsonify(users)

# example: localhost:5000/user/3
@app.get('/user/<int:id>')
def get_user_by_id(id):
  users = get('SELECT * FROM users WHERE id = :id', { 'id': id })
  return jsonify(dict(users[0]))

#Print our all artist name
all_artist = get ('SELECT name FROM artists')
#Print out oldest album
oldest_albums = get ('SELECT al_name, MIN(year_released) FROM albums JOIN name ')
#Uppdate albums without year_released with some year
#Adding data: add an artist 
#Adding data: add an album to artist
#Adding data : add a song to album
#Deliting data: delete an artist
#Deliting data: delete an album
#Deliting data: delete an album
#Average duration of songs
#Show the longest song from each album
#Number of songs each artist has 
#Search artist 
#Search songs 