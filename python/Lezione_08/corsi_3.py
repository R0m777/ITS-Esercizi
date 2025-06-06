from corsi_2 import Student,Group

class Course:
    def __init__(self, name: str):
        self.name: str = name
        self.groups:list = [Group]

    def register(self, student:Student) -> bool:
        for group in self.groups:
            if len(group.get_students()) < group.get_limit():
                if group.add_student(student):
                    return True
        return False

    def get_groups(self) ->list:
        return self.groups

    def add_group(self, group: Group) -> None:
        self.groups.append(group)