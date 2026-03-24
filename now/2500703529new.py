""" 
NAME : NANKABIRWA PRETTY CHRISTINE
REG NO. : 25/U/03529/EVE
STUDENT NO. : 2500703529
"""

ALLOWED_COURSES = ["CS1101", "CS1102", "CS1103", "CS1104", "CS1105"]

# CourseResult class
class CourseResult:
    def __init__(self,course_code,mark):
        self.course_code = course_code
        self.mark = mark
        self.grade_point = self.calculate_grade_point()

    def calculate_grade_point(self):
        if self.mark < 0 or self.mark > 100:
            print("Invalid mark")
            return 0
        
        if self.mark >= 80:
            return 5.0
        elif self.mark >= 70:
            return 4.0
        elif self.mark >= 60:
            return 3.0
        elif self.mark >= 50:
            return 2.0
        else:
            return 1.0
        
#Student Class
class Student:
    def __init__(self, name, reg_no, student_no):
        self.name = name
        self.reg_no = reg_no
        self.student_no = student_no
        self.results = {} #dictionary

    

