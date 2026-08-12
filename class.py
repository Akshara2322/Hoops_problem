# Class and Object
# Problem: Display Student Details

class Student:
    def student_details(self):
        name = input("Enter student name: ")
        mark = int(input("Enter mark: "))

        print("Student Name:", name)
        print("Mark:", mark)


student = Student()
student.student_details()