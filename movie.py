import csv
from typing import Collection
from dataclasses import dataclass
from datetime import date
import logging


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

    def is_release_this_year(self):
        """Check if movie release this year."""
        return self.year == date.today().year


class MovieCatalog:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance.movies = []
            cls._instance.load_movie_data()
        return cls._instance

    @staticmethod
    def unrecognized_format(row, m):
        log = logging.getLogger()
        log.error(f"Line {row}: Unrecognized format {', '.join(m)}")

    def load_movie_data(self):
        """Load movies from a CSV file line by line."""
        with open("movies.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            row = 0
            for m in reader:
                row += 1
                if not m or m[0] == '#':
                    # blank or comment line
                    continue
                if len(m) != 4:
                    self.unrecognized_format(row, m)
                    continue
                try:
                    title = m[1]
                    year = int(m[2])
                    genres = m[3].split('|')
                    m = Movie(title=title, year=year, genre=genres)
                    self.movies.append(m)
                except ValueError:
                    self.unrecognized_format(row, m)
                    continue

    def get_movie(self, title, year=None):
        for m in self.movies:
            if title.lower() == m.title.lower() and (year is None or m.year == year):
                return m
