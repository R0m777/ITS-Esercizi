from abc import ABC, abstractmethod
from typing import List, Optional

class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self) -> str:
        pass

    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Role: {self.get_role()}"

class Course:  # Forward declare for type hinting in Student and Professor
    pass

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id: str = student_id
        self.courses: List[Course] = []

    def get_role(self) -> str:
        return "Student"

    def enroll(self, course: "Course") -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  # Also add this student to the course's student list

    def __str__(self) -> str:
        courses_str = ", ".join(course.course_code for course in self.courses) if self.courses else "No courses"
        return super().__str__() + f", ID: {self.student_id}, Enrolled in: [{courses_str}]"

class Department:
    def __init__(self, name: str) -> None:
        self.department_name: str = name
        self.professors: List["Professor"] = []
        self.courses: List[Course] = []

    def add_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor: "Professor") -> None:
        if professor not in self.professors:
            self.professors.append(professor)

    def __str__(self) -> str:
        courses_str = ", ".join(course.course_code for course in self.courses) if self.courses else "No courses"
        professors_str = ", ".join(prof.name for prof in self.professors) if self.professors else "No professors"
        return (f"Department: {self.department_name}\n"
                f"  Courses: [{courses_str}]\n"
                f"  Professors: [{professors_str}]")

class Professor(Person):
    def __init__(self, name: str, age: int, professor_id: str, department: Department) -> None:
        super().__init__(name, age)
        self.professor_id: str = professor_id
        self.department: Department = department
        self.courses: List[Course] = []

    def get_role(self) -> str:
        return "Professor"

    def assign_to_course(self, course: Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.set_professor(self)

    def __str__(self) -> str:
        courses_str = ", ".join(course.course_code for course in self.courses) if self.courses else "No courses"
        return (super().__str__() + f", ID: {self.professor_id}, Department: {self.department.department_name}, "
                f"Teaching: [{courses_str}]")

class Course:
    def __init__(self, name: str, code: str) -> None:
        self.course_name: str = name
        self.course_code: str = code
        self.students: List[Student] = []
        self.professor: Optional[Professor] = None

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)
            if self not in student.courses:
                student.courses.append(self)

    def set_professor(self, professor: Professor) -> None:
        self.professor = professor
        if self not in professor.courses:
            professor.courses.append(self)

    def __str__(self) -> str:
        professor_name = self.professor.name if self.professor else "Not assigned"
        student_names = ", ".join(student.name for student in self.students) if self.students else "No students"
        return (f"Course: {self.course_name} ({self.course_code}), Professor: {professor_name}, "
                f"Students: [{student_names}]")

class University:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.departments: List[Department] = []
        self.students: List[Student] = []

    def add_department(self, department: Department) -> None:
        if department not in self.departments:
            self.departments.append(department)

    def add_student(self, student: Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def __str__(self) -> str:
        dept_names = ", ".join(dept.department_name for dept in self.departments) if self.departments else "No departments"
        student_names = ", ".join(student.name for student in self.students) if self.students else "No students"
        return (f"University: {self.name}\nDepartments: [{dept_names}]\nStudents: [{student_names}]")

# Driver code example
if __name__ == "__main__":
    # Create University
    uni = University("Example University")

    # Create Departments
    cs = Department("Computer Science")
    lit = Department("Literature")

    # Add departments to university
    uni.add_department(cs)
    uni.add_department(lit)

    # Create Courses
    ds = Course("Data Structures", "CS101")
    algo = Course("Algorithms", "CS102")
    medieval = Course("Medieval Literature", "LIT201")

    # Add courses to departments
    cs.add_course(ds)
    cs.add_course(algo)
    lit.add_course(medieval)

    # Create Professors
    prof_smith = Professor("John Smith", 45, "P1001", cs)
    prof_jones = Professor("Emily Jones", 50, "P1002", lit)

    # Add professors to departments
    cs.add_professor(prof_smith)
    lit.add_professor(prof_jones)

    # Assign professors to courses
    prof_smith.assign_to_course(ds)
    prof_smith.assign_to_course(algo)
    prof_jones.assign_to_course(medieval)

    # Create Students
    anna = Student("Anna Taylor", 20, "S2001")
    bob = Student("Bob Lee", 22, "S2002")

    # Add students to university
    uni.add_student(anna)
    uni.add_student(bob)

    # Enroll students in courses
    anna.enroll(ds)
    anna.enroll(medieval)
    bob.enroll(algo)
    bob.enroll(medieval)

    # Print university info step by step
    print(uni)
    print()

    print(cs)
    print(lit)
    print()

    print(ds)
    print(algo)
    print(medieval)
    print()

    print(anna)
    print(bob)
    print()

    print(prof_smith)
    print(prof_jones)
