import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
    
	def setUp(self):
		"""Test fixture contains:
    	
    	c = a customer
    	movies = list of some movies
    	"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", 2024, ["Adventure", "Kid", "History"])
		self.regular_movie = Movie("CitizenFour", 1990, ["Thriller"])
		self.childrens_movie = Movie("Frozen", 2019, ["Family", "Childrens"])
    	
	@unittest.skip("No convenient way to test")
	def test_billing():
		# no convenient way to test billing since its buried in the statement() method.
		pass
    
	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])

	def test_total_charge(self):
		"""Test total_charge method, check if it computes the price correct after add new rental."""
		movie1 = Rental(self.new_movie, 4)
		self.c.add_rental(movie1)
		self.assertEqual(self.c.get_total_charge(), movie1.get_price())
		movie2 = Rental(self.childrens_movie, 3)
		self.c.add_rental(movie2)
		self.assertEqual(self.c.get_total_charge(), movie1.get_price() + movie2.get_price())
		movie3 = Rental(self.regular_movie, 6)
		self.c.add_rental(movie3)
		self.assertEqual(self.c.get_total_charge(), movie1.get_price() + movie2.get_price() + movie3.get_price())

	def test_total_rental_points(self):
		"""Test total_rental_points method, check if it computes the point correct after add new rental."""
		movie1 = Rental(self.new_movie, 4)
		self.c.add_rental(movie1)
		self.assertEqual(self.c.get_total_rental_points(), movie1.get_rental_points())
		movie2 = Rental(self.childrens_movie, 3)
		self.c.add_rental(movie2)
		self.assertEqual(self.c.get_total_rental_points(), movie1.get_rental_points() + movie2.get_rental_points())
		movie3 = Rental(self.regular_movie, 6)
		self.c.add_rental(movie3)
		self.assertEqual(self.c.get_total_rental_points(),
						 movie1.get_rental_points() + movie2.get_rental_points() + movie3.get_rental_points())
