import csv
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


class MovieCatalog:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = []
            cls._instance.load_movie_data()
        return cls._instance

    def load_movie_data(self):
        """Load movies from a CSV file line by line."""
        with open("movies.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                title = row[1]
                year = row[2]
                genres = row[3].split('|')
                m = Movie(title=title, year=year, genre=genres)
                self.movies.append(m)

    def get_movie(self, title, year=None):
        for m in self.movies:
            if title.lower() == m.title.lower() and (year is None or m.year == year):
                return m
