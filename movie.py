from typing import Collection
from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Movie:
    """
    Class for keeping track of movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def __str__(self):
        return self.title

    def is_genre(self, genre):
        """Check if the given genre matches any of the movie’s genre."""
        return genre.lower() in [this_genre.lower() for this_genre in self.genre]
