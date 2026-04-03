class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        if not name.strip():
            raise ValueError("Song name cannot be empty")
        if not artist.strip():
            raise ValueError("Artist cannot be empty")
        if not genre.strip():
            raise ValueError("Genre cannot be empty")

        self.name = name.strip()
        self.artist = artist.strip()
        self.genre = genre.strip()

        self._register_song()

    def _register_song(self):
        cls = self.__class__
        cls.count += 1
        cls.genres.add(self.genre)
        cls.artists.add(self.artist)
        cls.genre_count[self.genre] = cls.genre_count.get(self.genre, 0) + 1
        cls.artist_count[self.artist] = cls.artist_count.get(self.artist, 0) + 1

    def __str__(self):
        return f"{self.name} by {self.artist} ({self.genre})"

    @classmethod
    def get_total_songs(cls):
        return cls.count