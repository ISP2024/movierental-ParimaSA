import logging
from pricing import PriceStrategy
from movie import Movie


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	For simplicity of this application only days_rented is recorded.
	"""

	def __init__(self, movie, days_rented, price_code):
		"""Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
		if not issubclass(price_code, PriceStrategy):
			log = logging.getLogger()
			log.error(f"Movie {movie.title} has unrecognized priceCode {price_code}")
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = price_code


	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price_code(self):
		# get the price code
		return self.price_code

	def get_price(self):
		"""Compute the price of rental."""
		return self.price_code().get_price(self.days_rented)

	def get_rental_points(self):
		"""Compute the renter points based on movie price code"""
		return self.price_code().get_rental_points(self.days_rented)
