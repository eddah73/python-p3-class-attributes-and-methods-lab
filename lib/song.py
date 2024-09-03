class Song:
    count  = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls,genre_to_add):
        if genre_to_add not in cls.genre_count:
            cls.genres.append(genre_to_add)

    @classmethod
    def add_to_artists(cls,artist_to_add):
        if artist_to_add not in cls.artist_count:
            cls.artists.append(artist_to_add)
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    @classmethod
    def find_artist_with_most_songs(cls):
        try:
            return max(
                cls.artist_count, key=lambda artist_name: cls.artist_count.get(artist_name, 0)
            )
        except Exception as e:
            print(e)
            return False


       
                

    

# s1 = Song("99 Problems", "Jay-Z", "Rap")
# s2 = Song("Halo", "Depeche Mode", "New Wave")
# s3 = Song("Clean", "Depeche Mode", "New Wave")
# s4 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# s5 = Song("Happy Birthday, What Am I Here For?", "Kahimi Kari", "Pop")
# print(Song.count)
# print(Song.genres)
# print(Song.artists)
# print(Song.genre_count)
# print(Song.artist_count)