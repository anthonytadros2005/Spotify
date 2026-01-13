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

@app.get("/")
def hello_world():
    return "<p>Hello, World</p>"


@app.get("/george")
def insult_george():
    return "<p>Get off your phone ya hiwan</p>"

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
        token_info = sp_oauth.refresh_access_token(token['refresh_token'])
        session['token'] = token_info

    return token





@app.get('/callback')
def getAccessToken():
    return 'your'