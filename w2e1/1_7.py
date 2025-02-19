class Student:
    def __init__(self, name: str, courses: list[str]):
        self.name = name
        self.courses = courses

    def attends(self, course: str) -> bool:
        return course in self.courses
