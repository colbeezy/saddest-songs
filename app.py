from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__)



@app.route("/")
def test():
    results = sp.search(q='eminem', limit=20)
    enumeratedResults = list(enumerate(results['tracks']['items']))
    return render_template('message.html', enumeratedResults=enumeratedResults)

if __name__ == "__main__":
    app.run()