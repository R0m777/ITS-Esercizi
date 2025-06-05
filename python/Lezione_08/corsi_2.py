class Person:
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, CF: {self.cf}, Age: {self.age}"


class Student(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group


class Lecturer(Person):
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)


class Group:
    def __init__(self, name: str, limit: int):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []

    def get_name(self) -> str:
        return self.name

    def get_limit(self) -> int:
        return self.limit

    def get_students(self) -> list[Student]:
        return self.students

    def get_limit_lecturers(self) -> int:
        return max(1, len(self.students) // 10)

    def add_student(self, student: Student) -> bool:
        if len(self.students) < self.limit:
            self.students.append(student)
            student.set_group(self)
            return True
        else:
            return False

    def add_lecturer(self, lecturer: Lecturer) -> bool:
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        else:
            return False

class Course:
    def __init__(self, name: str):
        self.name = name
        self.groups: list[Group] = []

    def get_groups(self) -> list[Group]:
        return self.groups

    def add_group(self, group: Group) -> None:
        self.groups.append(group)
    
    def register(self, student: Student) -> bool:
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                if group.add_student(student):
                    return True
        return False






def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    contatto = {"profile": name}
    if email is not None:
        contatto["email"] = email
    contatto["telefono"] = telefono
    return contatto

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    if dictionary.get("profile") == name:
        if email is not None:
            dictionary["email"] = email
        if telefono is not None:
            dictionary["telefono"] = telefono
    return dictionary



def rimbalzo():
    altezza:float = 0.0  
    velocita:float = 100.0  
    tempo:int = 0  
    rimbalzi:int = 0

    while rimbalzi < 5:
        
        if altezza < 0:  
            print(f"Tempo: {tempo} Rimbalzo!")
            altezza *= -0.5 
            velocita *= -0.5 
            rimbalzi += 1  
            tempo += 1  
        else:
            print(f"Tempo: {tempo} Altezza: {altezza:.1f}")
            altezza += velocita  
            velocita -= 96
            tempo +=1  





