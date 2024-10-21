class Student:
    def __init__(self, name: str, code: int) -> None:
        self._name = name
        self._code = code

    def get_name(self) -> str:
        return self._name

    def get_code(self) -> int:
        return self._code

    def show_infos(self) -> None:
        print(f"Student: {self._name} || Registration: {self._code}")

class Course:
    def __init__(self, name: str, code: int) -> None:
        self._name = name
        self._code = code
        self.list_students = []

    def add_student(self, student) -> None:
        new_student = Student(student.get_name(), student.get_code())
        self.list_students.append(new_student)

        print("New student added!")
    
    def get_name(self) -> str:
        return self._name

    def get_code(self) -> int:
        return self._code

    def show_infos(self) -> None:
        print(f"Course: {self._name} || Code: {self._code}")

    def show_students(self) -> None:
        for student in self.list_students:
            student.show_infos()

class School:
    def __init__(self, name: str, code: int) -> None:
        self._name = name
        self._code = code
        self.list_courses = []

    def add_course(self, course) -> None:
        new_course = Course(course.get_name(), course.get_code())
        self.list_courses.append(new_course)

        print("New course added!")

    def show_infos(self) -> None:
        print(f"School Name: {self._name}")

    def show_courses(self) -> None:
        for course in self.list_courses:
            course.show_infos()

# Create objects

student01 = Student("Carlos", 1234)
student02 = Student("Vinicius", 1235)
student03 = Student("Monteiro", 1236)
student04 = Student("Souza", 1237)

course01 = Course("POO Python", 112233)
course02 = Course("Java POO", 112244)

school = School("Creche dos Adultos - CMZL", 696)

# Add students to courses
course01.add_student(student01)
course01.add_student(student03)
course02.add_student(student02)
course02.add_student(student04)
print("\n")

# Add courses to school
school.add_course(course01)
school.add_course(course02)
print("\n")

# Show students
course01.show_students()
course02.show_students()
print("\n")

# Show courses
school.show_infos()
school.show_courses()