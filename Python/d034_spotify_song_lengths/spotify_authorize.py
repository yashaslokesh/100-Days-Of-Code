import webbrowser
import sys
from requests_oauthlib import OAuth2Session
import os

### Begin Authorization ###

def authorize():
    token_url = "https://accounts.spotify.com/api/token"
    auth_url = "https://accounts.spotify.com/authorize/"

    client_id = os.environ.get("SONG_VISUALIZER_CLIENT_ID")
    client_secret = os.environ.get("SONG_VISUALIZER_CLIENT_SECRET")
    redirect_uri = "http://google.com/"

    oauth = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
    auth_url, state = oauth.authorization_url(url=auth_url)

    webbrowser.open(auth_url)

    response = input("\nEnter the callback url after authorizing, then click enter twice: ")

    if 'access_denied' not in response:
        print("Success")
    else:
        sys.exit("You denied this script access to your Spotify account, please run this script again.")

    token = oauth.fetch_token(
        token_url=token_url,
        authorization_response=response,
        client_secret=client_secret
    )

    print('Authentication successful')

    return oauth

### End Authorization ###
# Use oauth.[HTTP Method] to perform actions with Spotify Web API endpoints