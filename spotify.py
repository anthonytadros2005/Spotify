import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy.oauth2 as oauth2
load_dotenv()
client_id=os.getenv("SPOTIPY_CLIENT_ID")
client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
SCOPES = "user-read-private user-library-read playlist-modify-private"
redirect_uri = 'http://127.0.0.1:5000/callback'
# credentials = oauth2.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=SCOPES)
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope=SCOPES,
#         open_browser=True
#
#     )
# )
#
# me = sp.current_user()
# print("Logged in as:", me["display_name"])
# Moods = ["Calm", "Hype", "Focus", "Sad", "Happy"]
# Separate_Mood_Lists = {mood: [] for mood in Moods}
#
#
#
# def get_all_liked_songs(sp):
#     songs = []
#     limit = 50
#     offset = 0
#
#     while True:
#         results = sp.current_user_saved_tracks(limit=limit, offset=offset)
#         items = results["items"]
#         songs.extend(items)
#         print(f"Fetched {len(songs)} liked songs so far...")
#         if len(items) < limit:
#             break
#         offset += limit
#     return songs
#
# liked_songs =get_all_liked_songs(sp)
# print("The total liked songs =", len(liked_songs))
#
#
#
# def classify_moods(track):
#     name = (track.get("name") or "").lower()
#     duration = track.get("duration_ms", 0)
#     popularity = track.get("popularity", 0)
#     if any(w in name for w in["sad", "heartbreak", "cry", "hurt", "lonely", "alone", "tear"]):
#         return "Sad"
#     if any(w in name for w in["happy", "smile", "good"]):
#         return "Happy"
#     if any(w in name for w in ["remix", "dance", "party"]):
#         return "Hype"
#     if popularity >= 75:
#         return "Hype"
#     if duration >= 240_000:
#         return "Focus"
#     if popularity <= 30:
#         return "Calm"
#     return "Happy"
#
#
#
# for item in liked_songs:
#     track = item.get("track")
#     if not track:
#         continue
#
#     uri = track.get("uri")
#     if not uri:
#         continue
#
#     mood = classify_moods(track)
#     Separate_Mood_Lists[mood].append(uri)
#
# for mood in Moods:
#     print(mood, "=", len(Separate_Mood_Lists[mood]))
#
# user_id = sp.current_user()["id"]
# def get_playlists(sp):
#     playlists = {}
#     limit = 50
#     offset = 0
#
#     while True:
#         results = sp.current_user_playlists(limit=limit, offset = offset)
#         items = results["items"]
#
#         for playlist in items:
#             playlists[playlist["name"]] = playlist["id"]
#
#         if len(items) < limit:
#             break
#
#         offset += limit
#
#     return playlists
#
# def create_or_get_playlist(sp, user_id, name, playlists):
#     if name in playlists:
#         return playlists[name]
#
#     playlist = sp.user_playlist_create(user=user_id, name=name, public=False)
#     return playlist["id"]
#
# def get_playlist_songs(sp, playlist_id):
#     tracks = set()
#     limit = 100
#     offset = 0
#
#     while True:
#         results = sp.playlist_items(playlist_id, limit=limit, offset=offset)
#         items = results["items"]
#
#         for item in items:
#             track = item.get("track")
#             if track:
#                 tracks.add(track["uri"])
#
#         if len(items) < limit:
#             break
#
#         offset += limit
#     return tracks
#
#
# def add_songs_to_playlist(sp, playlist_id, song_uris):
#     existing = get_playlist_songs(sp, playlist_id)
#     new_songs = [uri for uri in song_uris if uri not in existing]
#     if new_songs:
#         sp.playlist_add_items(playlist_id, new_songs)
#
#
# playlists = get_playlists(sp)
# for mood in Moods:
#     playlist_name = f"Mood: {mood}"
#
#     playlist_id = create_or_get_playlist(
#         sp,
#         user_id,
#         playlist_name,
#         playlists
#     )
#
#     add_songs_to_playlist(
#         sp,
#         playlist_id,
#         Separate_Mood_Lists[mood]
#     )
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#






