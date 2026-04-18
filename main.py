class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} soat)"


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"  {self.name} -> '{course.title}' kursiga yozildi")

    def show_courses(self):
        print(f"\n{self.name}ning kurslari ({len(self.courses)}):\n")
        for i, c in enumerate(self.courses, 1):
            print(f"  {i}. {c}")


if __name__ == "__main__":
    t = Student("Anvor")
    t.enroll(Course("Python", 40))
    t.enroll(Course("Matematika", 30))
    t.enroll(Course("Ingliz tili", 50))
    t.show_courses()
