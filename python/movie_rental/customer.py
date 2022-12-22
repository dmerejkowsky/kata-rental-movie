from movie_rental.movie import Movie


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_statement(self):
        total_amount = 0.0
        frequent_renter_points = 0
        result = f"Rental record for {self.name}\n"
        for rental in self.rentals:
            this_amount = 0.0

            # Determine amount for each line
            if rental.movie.price_code == Movie.REGULAR:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif rental.movie.price_code == Movie.NEW_RELEASE:
                this_amount += rental.days_rented * 3
            elif rental.movie.price_code == Movie.CHILDREN:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1

            # add bonus for a two day new release rental
            if rental.movie.price_code == Movie.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += f"\t{rental.movie.title}\t{this_amount}\n"
            total_amount += this_amount

        # add footer lines
        result += f"Amount owed is {total_amount}\n"
        result += f"You earned {frequent_renter_points} frequent renter points\n"
        return result
