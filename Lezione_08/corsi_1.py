class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = 2 * seats

    def get_id(self) -> str:
        return self.id

    def get_floor(self) -> int:
        return self.floor

    def get_seats(self) -> int:
        return self.seats

    def get_area(self) -> int:
        return self.area


class Building:
    def __init__(self, name: str, address: str, floors: tuple[int, int]):
        self.name = name
        self.address = address
        self.floors = floors 
        self.rooms = []

    def get_floors(self) -> tuple[int, int]:
        return self.floors

    def get_rooms(self) -> list[Room]:
        return self.rooms

    def add_room(self, room: Room) -> None:
        existing_ids = []
        for r in self.rooms:
            existing_ids.append(r.get_id())
        if self.floors[0] <= room.get_floor() <= self.floors[1] and room.get_id() not in existing_ids:
           self.rooms.append(room)
    
    def area(self) -> int:
        total_area = 0
        for room in self.rooms: 
            total_area += room.get_area()
        return total_area

