import unittest
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", 2024, "Adventure")
		self.regular_movie = Movie("Air", 2020, ["Comedy", "Kid"])
		self.childrens_movie = Movie("Frozen", 2019, ["Family", "Kid"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", 2020, ["Comedy", "Kid"])
		self.assertEqual("Air", m.title)

	def test_rental_price(self):
		"""Test get_price method in rental, check if it returns correct price."""
		# New Release Movie
		rental = Rental(self.new_movie, 1, NewRelease)
		self.assertEqual(rental.get_price(), 3*1)
		rental = Rental(self.new_movie, 5, NewRelease)
		self.assertEqual(rental.get_price(), 3*5)
		# Regular Movie
		rental = Rental(self.regular_movie, 2, RegularPrice)
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 6, RegularPrice)
		self.assertEqual(rental.get_price(), (2 + (4*1.5)))
		# Children Movie
		rental = Rental(self.childrens_movie, 3, ChildrenPrice)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 7, ChildrenPrice)
		self.assertEqual(rental.get_price(), (1.5 + (4 * 1.5)))

	def test_rental_points(self):
		"""Test rental_points method in rental, check if it returns correctly."""
		# New Release Movie
		rental = Rental(self.new_movie, 3, NewRelease)
		self.assertEqual(rental.get_rental_points(), 3)
		rental = Rental(self.new_movie, 15, NewRelease)
		self.assertEqual(rental.get_rental_points(), 15)
		# Regular Movie
		rental = Rental(self.regular_movie, 2, RegularPrice)
		self.assertEqual(rental.get_rental_points(), 1)
		# Children Movie
		rental = Rental(self.childrens_movie, 8, ChildrenPrice)
		self.assertEqual(rental.get_rental_points(), 1)
