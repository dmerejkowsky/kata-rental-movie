import textwrap
from movie_rental.movie import Movie
from movie_rental.rental import Rental
from movie_rental.customer import Customer


def test_statement_for_regular_movie():
    movie1 = Movie("Gone with the Wind", Movie.REGULAR)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer = Customer("Sallie")
    customer.rentals = [rental1]

    actual = customer.get_statement()

    expected = textwrap.dedent(
        """\
        Rental record for Sallie
        \tGone with the Wind\t3.5
        Amount owed is 3.5
        You earned 1 frequent renter points
        """
    )
    assert actual == expected


def test_statement_for_new_release_movie():
    movie1 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer = Customer("Sallie")
    customer.rentals = [rental1]

    actual = customer.get_statement()
    expected = textwrap.dedent(
        """\
        Rental record for Sallie
        \tStar Wars\t9.0
        Amount owed is 9.0
        You earned 2 frequent renter points
        """
    )
    assert actual == expected


def test_statement_for_children_movie():
    movie1 = Movie("Madagascar", Movie.CHILDREN)
    rental1 = Rental(movie1, 3)  # 3 day rental
    customer = Customer("Sallie")
    customer.rentals = [rental1]

    actual = customer.get_statement()
    expected = textwrap.dedent(
        """\
        Rental record for Sallie
        \tMadagascar\t1.5
        Amount owed is 1.5
        You earned 1 frequent renter points
        """
    )
    assert actual == expected


def test_statement_for_many_movies():
    movie1 = Movie("Madagascar", Movie.CHILDREN)
    rental1 = Rental(movie1, 6)  # 6 day rental
    movie2 = Movie("Star Wars", Movie.NEW_RELEASE)
    rental2 = Rental(movie2, 2)  # 2 day rental
    movie3 = Movie("Gone with the Wind", Movie.REGULAR)
    rental3 = Rental(movie3, 8)  # 8 day rental
    customer = Customer("David")
    customer.rentals = [rental1, rental2, rental3]

    actual = customer.get_statement()

    expected = textwrap.dedent(
        """\
        Rental record for David
        \tMadagascar\t6.0
        \tStar Wars\t6.0
        \tGone with the Wind\t11.0
        Amount owed is 23.0
        You earned 4 frequent renter points
        """
    )
    assert actual == expected
