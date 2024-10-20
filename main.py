# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer
from pricing import ChildrenPrice, RegularPrice, NewRelease

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", 2024, ["Kid", "Adventure"]),
        Movie("Oppenheimer", 2023, ["History", "Action"]),
        Movie("Frozen", 2022, ["children", "Family"]),
        Movie("Bitconned", 2024, ["Tech"]),
        Movie("Particle Fever", 2019, ["Action"])
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    movie = make_movies()
    for n in range(len(movie)):
        customer.add_rental(Rental(movie[n], days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
