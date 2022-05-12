from film import Film


class IterPage:
    def __init__(self, films: list) -> None:
        self.film = films
        self.count_page = len(films)
        self.current_page = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current_page < self.count_page:
            self.count_page += 1
            return 