import json
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d034_spotify_song_lengths")

import spotify_authorize as sa

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

def get_stats(user, playlist_id, oauth):
    response = oauth.get(f"https://api.spotify.com/v1/users/{user}/playlists/{playlist_id}/tracks?offset=0")
    data = json.loads(response.text)

    lengths = [item["track"]["duration_ms"] for item in data["items"]]
    popularities = [item["track"]["popularity"] for item in data["items"]]
    next_query = data["next"]

    while next_query != None:
        response = oauth.get(next_query)
        data = json.loads(response.text)

        lengths += [item["track"]["duration_ms"] for item in data["items"]]
        popularities += [item["track"]["popularity"] for item in data["items"]]
        next_query = data["next"]

    print(f"Total # of songs: {len(lengths)}")

    lengths = np.divide(lengths, 1000)

    print(f"Longest song length: {max(lengths)}")

    max_pop = max(popularities)
    min_pop = min(popularities)

    # Map numbers from min_pop to max_pop range to the 0-100 range for relative popularities
    popularities = np.multiply(np.subtract(popularities, min_pop), 100/(max_pop - min_pop))

    # low2 + (value - low1) * (high2 - low2) / (high1 - low1)

    return lengths, popularities

def plot_results(song_lengths : list, popularities : list):
    plt.figure(figsize=(10,10))
    plt.scatter(song_lengths, popularities, marker='.', c='c')

    plt.axis([min(song_lengths), max(song_lengths), 0, 100])
    plt.xlabel('Length')
    plt.ylabel('Popularity')
    plt.title('Song length vs. popularity')
    # plt.axis()
    plt.show()

def main():
    oauth = sa.authorize()
    input()
    user = input("Enter desired user to retrieve their public playlists: ")
    playlist_id = get_playlist(user, oauth)
    song_lengths, popularities = get_stats(user, playlist_id, oauth)
    plot_results(song_lengths, popularities)

if __name__ == '__main__':
    main()