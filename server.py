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
# Lista ut alla artister i en template. Visa namn och bild
# Skapa en detaljsida för en artist, som innehåller name, description, bild och en lista på albums. När man klickar på en artist från listan i nr 18 går man till detaljsidan
# Albums på detaljsidan för en artist ska visa titel, bild, antal låtar och total duration
# Skapa en detaljsida för ett album, som innehåller title, description, bild, antal låtar, total duration och en lista på låtar
# Låtarna på detaljsidan för ett album ska visa index, name och duration
# Lägg till input för att kunna söka på artister, album och låtar. Klickar man på något i resultatlistan ska samma hända som tidigare: artist och album går till detaljsidan, en låt spelar den i en player
# När man klickar på en låt ska låten spelas i en YouTube player på sidan
# Skapa formulär för att kunna lägga till artister, album och låtar