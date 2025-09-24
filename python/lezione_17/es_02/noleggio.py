from film import Film


class Noleggio:
    
    def __init__(self, flim_list:list):
    
        self.flim_list = flim_list
        self.rented_film = {}

    def isAvailable(self, film):
        for f in self.flim_list:
            if f.isEqual(film):
                print(f"Il film scelto è disponibile: {f.getTitle}!")
                return True
            else:
                print(f"Il film scelto non è disponibile: {f.getTitle}!")
                return False

