import logging
from pricing import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, price_code):
        # Initialize a new movie.
        if not issubclass(price_code, PriceStrategy):
            log = logging.getLogger()
            log.error(f"Movie {title} has unrecognized priceCode {price_code}")
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
