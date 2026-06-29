class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def teacher_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


teacher = Teacher("John Doe", 35, "Mathematics")
student = Student("Jane Smith", 20, "A")

teacher.teacher_info()
student.student_info()