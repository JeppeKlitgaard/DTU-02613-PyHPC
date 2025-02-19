class Student:
    def __init__(self, name: str, courses: list[str]):
        self.name = name
        self.courses = courses

    def attends(self, course: str) -> bool:
        return course in self.courses


def coursestudents(students: list[Student], course: str) -> list[Student]:
    students_in_course = filter(lambda x: x.attends(course), students)
    return [student.name for student in students_in_course]