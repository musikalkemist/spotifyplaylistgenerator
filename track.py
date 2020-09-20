class Track:
    """Track represents a piece of music."""

    def __init__(self, name, id, artist):
        """
        :param name (str): Track name
        :param id (int): Spotify track id
        :param artist (str): Artist who created the track
        """
        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return self.name + " by " + self.artist