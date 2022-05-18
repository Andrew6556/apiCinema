from film import Film


class IterPage:
    def __init__(self, films) -> None:
        self.films = films
        self.count_page = len(films)
        self.current_page = 0
    
    def __iter__(self) -> object:
        return self

    def __next__(self) -> list:
        if self.current_page < self.count_page:
            self.current_page += 1
            return self.films[self.current_page - 1]

        raise StopIteration