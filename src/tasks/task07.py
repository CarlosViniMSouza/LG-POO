class Student:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def show_infos(self):
        print(f"Name student: {self.name} \nRegistration: {self.code}")

class Course:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        # self.list_students = [Student(name, code)]
        self.list_students = []

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def show_infos(self):
        print(f"Name course: {self.name} \nCode: {self.code}")
    
    # @classmethod
    def add_student(self, student):
        new_student = Student(student.get_name(), student.get_code())
        self.list_students.append(new_student)

        print("New student added!")

    # @classmethod
    def show_students(self):
        for student in self.list_students:
            student.show_infos()

            #print(f"List all students: {student.show_info()}")

class School:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        # self.list_courses = [Course(name, code)]
        self.list_courses = []

    def show_infos(self):
        print(f"School name: {self.name}")

    # @classmethod
    def add_course(self, course):
        new_course = Course(course.get_name(), course.get_code())
        self.list_courses.append(new_course)

        print("New course added!")

    # @classmethod
    def show_courses(self):
        for course in self.list_courses:
            course.show_infos()

            # print(f"List all courses: {self.list_courses}")

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