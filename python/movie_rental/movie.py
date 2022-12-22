class Movie:
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2

    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def __repr__(self):
        return f"Movie({self.title})"
