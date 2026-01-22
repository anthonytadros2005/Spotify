import spotipy

from venv import create

from flask import Flask, redirect, request, session, url_for
import os
from dotenv import load_dotenv
from spotify import sp_oauth, redirect_uri
import urllib.parse
load_dotenv()


var = 'https://accounts.spotify.com/authorize?'

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.get('/login')
def login():
    redirect_url = sp_oauth.get_authorize_url()
    return redirect(redirect_url)

@app.get('/callback')
def callback():
    code = request.args.get('code')
    token = sp_oauth.get_access_token(code)
    session['token'] = token
    return redirect(url_for('profile'))


@app.get('/profile')
def profile():
    token_info = get_token()
    if not token_info:
        return redirect(url_for('login'))
    sp = spotipy.Spotify(auth=token_info['access_token'])
    user = sp.current_user()
    return user


def get_token():
    token = session.get('token', None)
    if not token:
        return None
    if sp_oauth.is_token_expired(token):
        token = sp_oauth.refresh_access_token(token['refresh_token'])
        session['token'] = token

    return token
@app.get('/run')
def run():
    token_info = get_token()
    if not token_info:
        return redirect(url_for('login'))
    sp = spotipy.Spotify(auth=token_info['access_token'])
    liked_songs = get_all_liked_songs(sp)
    return f"Total liked songs: {len(liked_songs)}"


def get_all_liked_songs(sp):
     songs = []
     limit = 50
     offset = 0

     while True:
         results = sp.current_user_saved_tracks(limit=limit, offset=offset)
         items = results["items"]
         songs.extend(items)
         print(f"Fetched {len(songs)} liked songs so far...")
         if len(items) < limit:
             break
         offset += limit
     return songs


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
