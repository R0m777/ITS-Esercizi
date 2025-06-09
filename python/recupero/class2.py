class Movie:
    def __init__(self, movie_id:str, title:str, director:str, is_rented:bool=False):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def rent(self) -> None:
        if not self.is_rented:
            self.is_rented = True
        else:
            print(f"il film {self.title} è già noleggiato")

    def return_movie(self) -> str:
        if self.is_rented:
            self.is_rented = False
        else:
            return f"Il film '{self.title}' non è stato noleggiato da questo cliente."
        

class Custumer:
    def __init__(self, custumer_id:str, custumer_name:str, rented_movies: list[Movie] = []):
        self.custumer_id = custumer_id
        self.custumer_name = custumer_name
        self.rented_movies = rented_movies     

    def rent_movie(self, movie:Movie) -> None:
        if not movie.is_rented:
            movie.rent()
            self.rented_movies.append(movie)
        else:
            print(f"il film è stato affitato")

    def return_movie(self, movie:Movie) -> None:
        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)
        else:
            print(f"il film non è stato affittato")


class VideoRentalStore:
    def __init__(self, movies:dict[str,Movie] = {}, customers: dict[str,Custumer] = {}):
        self.movies = movies
        self.customers = customers

    def add_movie(self, movie_id: str, title: str, director: str):
        if movie_id in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")
        else:
            self.movies[movie_id] = Movie(movie_id, title, director)

    def register_customer(self, customer_id: str, name: str):
        if customer_id in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")
        else:
            self.customers[customer_id] = Custumer(customer_id, name)

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if customer and movie:
            customer.rent_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def return_movie(self, customer_id: str, movie_id: str) -> None:
        customer = self.customers.get(customer_id)
        movie = self.movies.get(movie_id)

        if customer and movie:
            customer.return_movie(movie)
        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str)-> list:
        customer = self.customers.get(customer_id)
        if customer:
            return customer.rented_movies
        else:
            print("Cliente non trovato.")
            return []

    def get_all_rented_movies(self)-> list:
        rented_movies:list = []
        for movie in self.movies.values():
            if movie.is_rented:
                rented_movies.append(movie)
        return rented_movies




