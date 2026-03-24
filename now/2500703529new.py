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

    def calculate_grade(self):