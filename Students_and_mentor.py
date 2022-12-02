class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def _get_average_hw_grade(self):
        average_grade = sum(self.grades.values() / len(self.grades))
        return average_grade

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {self._get_average_hw_grade():.2f}\
        \n Курсы в процессе изучения: {*self.courses_in_progress,}\n Завершенные курсы: {*self.finished_courses,}'
        return res 

    def __lt__(self, dif_student):
        value1 = self._get_average_hw_grade()
        value2 = dif_student._get_average_hw_grade()
        if value1 < value2:
            return True
        else:
            return False
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_average_lecture_grade(self):
        average_grade = sum(self.grades.values() / len(self.grades))
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self._get_average_lecture_grade():.2f}'
        return res

    def __lt__(self, dif_lecturer):
        value1 = self._get_average_lecture_grade()
        value2 = dif_lecturer._get_average_lecture_grade()
        if value1 < value2:
            return True
        else:
            return False

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)       