from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(PriceStrategy, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        """Get price of NewRelease movie: Straight $3 per day charge."""
        return 3 * days

    def get_rental_points(self, days: int) -> int:
        """New release rentals earn 1 point for each day rented."""
        return days


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        """Get price of Regular movie: two days for $2, additional days 1.50 per day."""
        price = 2.0
        if days > 2:
            price += 1.5 * (days - 2)
        return price

    def get_rental_points(self, days: int) -> int:
        """Get rental points for Regular movie: only one point for each"""
        return 1


class ChildrenPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_price(self, days: int) -> float:
        """Get price of Regular movie: three days for $1.50, additional days 1.50 per day."""
        price = 1.5
        if days > 3:
            price += 1.5 * (days - 3)
        return price

    def get_rental_points(self, days: int) -> int:
        """Get rental points for Children movie: only one point for each"""
        return 1
