class Song:
    count = 0
    artist_count = {}
    genre_count = {}
    genres = []
    artists = []
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_to_song_count()
        self.add_to_artist_count(artist)
        self.add_to_genre_count(genre)

    @classmethod
    def add_to_song_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        current = cls.artist_count.get(artist)
        if current == None:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] = current + 1

        cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):

        current = cls.genre_count.get(genre)
        if current == None:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] = current + 1
        cls.genres.append(genre)