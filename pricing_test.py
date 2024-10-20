import unittest
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class PricingTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2024, "Adventure")
        self.new_children_movie = Movie("Frozen2", 2024, ["Family", "Children"])
        self.regular_movie = Movie("Air", 2020, ["Comedy", "Kid"])
        self.childrens_movie1 = Movie("Frozen", 2019, ["Family", "Childrens"])
        self.childrens_movie2 = Movie("Nemo", 2020, ["Family", "children"])

    def test_price_code_for_movie(self):
        """Test if rental define correct price code."""
        # new release movie, movie release this year
        r = Rental(movie=self.new_movie, days_rented=4)
        self.assertEqual(r.price_code, NewRelease)
        r = Rental(movie=self.new_children_movie, days_rented=4)
        self.assertEqual(r.price_code, NewRelease)
        # children movie, movie with children or childrens genre
        r = Rental(movie=self.childrens_movie1, days_rented=2)
        self.assertEqual(r.price_code, ChildrenPrice)
        r = Rental(movie=self.childrens_movie2, days_rented=5)
        self.assertEqual(r.price_code, ChildrenPrice)
        # regular movie
        r = Rental(movie=self.regular_movie, days_rented=5)
        self.assertEqual(r.price_code, RegularPrice)
