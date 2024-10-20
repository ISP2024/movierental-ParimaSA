import unittest
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class RentalTest(unittest.TestCase):
    
	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", NewRelease)
		self.regular_movie = Movie("Air", RegularPrice)
		self.childrens_movie = Movie("Frozen", ChildrenPrice)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", RegularPrice)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(RegularPrice, m.get_price_code())

	def test_rental_price(self):
		"""Test get_price method in rental, check if it returns correct price."""
		# New Release Movie
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3*1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 3*5)
		# Regular Movie
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 6)
		self.assertEqual(rental.get_price(), (2 + (4*1.5)))
		# Children Movie
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 7)
		self.assertEqual(rental.get_price(), (1.5 + (4 * 1.5)))

	def test_rental_points(self):
		"""Test rental_points method in rental, check if it returns correctly."""
		# New Release Movie
		rental = Rental(self.new_movie, 3)
		self.assertEqual(rental.get_rental_points(), 3)
		rental = Rental(self.new_movie, 15)
		self.assertEqual(rental.get_rental_points(), 15)
		# Regular Movie
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_rental_points(), 1)
		# Children Movie
		rental = Rental(self.childrens_movie, 8)
		self.assertEqual(rental.get_rental_points(), 1)
