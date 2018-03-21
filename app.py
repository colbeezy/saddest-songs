from __future__ import division
from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util


client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def artist_lookup():
    """Lookup artist"""

    # if user reached route via POST
    if request.method == "POST":

        # Ensure artist was submitted
        if not request.form.get("artist"):
            return render_template("error.html")

        artist = request.form.get("artist")
        if not artist:
            return render_template("error.html")
        else:
            results = sp.search(q=artist, limit=50)
            enumeratedResults = list(enumerate(results['tracks']['items']))
            track_ids = []
            track_names = []
            for i, t in enumeratedResults:
                track_ids.append(t['uri'])
                track_names.append(t['name'])
            features = sp.audio_features(track_ids)
            track_valences = []
            for feature in features:
                track_valences.append('{0:.0f}%'.format(feature['valence']*100))
            namesAndVales = sorted(zip(track_names, track_valences), key=lambda x: x[1])
            return render_template('results.html', namesAndVales=namesAndVales)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("artist-lookup.html")



if __name__ == "__main__":
    app.run()