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

    def add_result(self, course_code, mark):
        if course_code in ALLOWED_COURSES:
            self.results[course_code] = CourseResult(course_code, mark)
        else:
            print("Invalid course code")

    def compute_cgpa(self):
        total = sum(result.grade_point for result in self.results.values())
        cgpa = total / len(self.results)
        return round(cgpa,2)

# function; passed courses
def get_passed_courses(student):
    passed = []
    for result in student.results.values():
        if result.mark >= 50:
            passed.append(result.course_code)
    return passed

