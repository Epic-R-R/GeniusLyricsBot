import lyricsgenius
token = "nVS9Fjlq7ftowDKzI6iVNf2Qo3CMYxLnYI5KHj4GYWA37PyPn-2rYaaMg7Mh4ypE"
def searchmusicgenius(name):
    genius = lyricsgenius.Genius(token)
    song = genius.search_song(name)
    # print(song.lyrics)
    print(song)

def searchartistgenius(name):
    genius = lyricsgenius.Genius(token)
    artist = genius.search_artist("Ali sorena", max_songs=3, sort="title")
    artist.save_lyrics() # save artist musics into JSON file
