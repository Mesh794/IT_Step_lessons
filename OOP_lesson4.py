class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Song):
            return (self.author, self.name) == (other.author, other.name)
        else:
            return False

    def __str__(self):
        return f"{self.author} пісня '{self.name}'"


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __iter__(self):
        for song in self.songs:
            yield song

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

song1 = Song("Imagine", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Shape of You", "Ed Sheeran")
song4 = Song("Imagine", "John Lennon")

playlist = Playlist([])
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
print(len(playlist))
print(song4 in playlist)
playlist.remove_song(song4)
for song in playlist:
    print(song)
