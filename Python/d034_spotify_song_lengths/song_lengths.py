import spotify_authorize as sa
import json
import numpy as np
import matplotlib.pyplot as plt

def get_playlist(user : str, oauth) -> str:
    response = oauth.get(f"https://api.spotify.com/v1/users/{user}/playlists?offset=0")
    data = json.loads(response.text)

    print("\nFormat:\nPlaylist ID  ->  Playlist Title\n")
    playlists = [f'{item["id"]}  ->  {item["name"]}' for item in data["items"]]
    next_query = data["next"]


    while next_query != None:
        response = oauth.get(next_query)
        data = json.loads(response.text)

        playlists += [f'{item["id"]}  ->  {item["name"]}' for item in data["items"]]
        next_query = data["next"]

    print('\n'.join(playlists) + "\n")

    playlist_id = input("Enter the playlist ID for corresponding to the playlist title that you want to analyze: ")
    return playlist_id.strip()

def get_song_lengths(user, playlist_id, oauth):
    response = oauth.get(f"https://api.spotify.com/v1/users/{user}/playlists/{playlist_id}/tracks?offset=0")
    data = json.loads(response.text)

    lengths = [item["track"]["duration_ms"] for item in data["items"]]
    next_query = data["next"]

    while next_query != None:

        response = oauth.get(next_query)
        data = json.loads(response.text)

        lengths += [item["track"]["duration_ms"] for item in data["items"]]
        next_query = data["next"]

    print(f"Total # of songs: {len(lengths)}")

    lengths = np.divide(lengths, 1000)

    print(f"Longest song length: {max(lengths)}")

    return lengths

def plot_results(song_lengths : list):
    n, bins, patch = plt.hist(song_lengths, 40, facecolor='b', alpha=0.5)

    plt.xlabel('Song Length (Seconds)')
    plt.ylabel('Frequency')
    plt.title('Frequency of Song lengths in playlist')
    # plt.axis()
    plt.show()

def main():
    oauth = sa.authorize()
    input()
    user = input("Enter desired user to retrieve their public playlists: ")
    playlist_id = get_playlist(user, oauth)
    song_lengths = get_song_lengths(user, playlist_id, oauth)
    plot_results(song_lengths)

if __name__ == '__main__':
    main()