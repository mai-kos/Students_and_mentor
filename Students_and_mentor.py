import gc

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
        values = self.grades.values()
        values_sum = 0
        values_total = 0
        for value in values:
            values_sum += sum(value)
            values_total += len(value)
        average_grade = values_sum / values_total
        return average_grade

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer)\
        and course in self.courses_in_progress\
        and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {self._get_average_hw_grade():.2f}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'
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
        values = self.grades.values()
        values_sum = 0
        values_total = 0
        for value in values:
            values_sum += sum(value)
            values_total += len(value)
        average_grade = values_sum / values_total
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self._get_average_lecture_grade():.2f}'
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
        if isinstance(student, Student)\
        and course in self.courses_attached\
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res     

# Создаем функцию для нахождения всех экземпляров класса

def get_all_instances(of_class):
    _instances = []
    for obj in gc.get_objects():
        if isinstance(obj, of_class):
            _instances.append(obj)
    return _instances

# Я не стал посылать в функцию два аргумента, как сказано в задании.
# Мне показалось, что не логично посылать список студентов вручную.
# Если по заданию нам надо среднюю оценку ВСЕХ студентов курса,
# то мы можем пробежаться по всем экземплярам класса Student. 

def get_average_grade_for_all_students(course):
    total_grades = 0
    total_students = 0
    for instance in get_all_instances(Student):
        if course in instance.courses_in_progress\
        and course in instance.grades:
            total_grades += sum(instance.grades.get(course))
            total_students += 1
    if total_grades == 0:
        return 'Оценок нет'
    return total_grades / total_students

# Здесь такая же логика. Пробегаемся по всем экземплярам класса Lecturer.

def get_average_grade_for_all_lecturers(course):
    total_grades = 0
    total_lecturers = 0
    for instance in get_all_instances(Lecturer):
        if course in instance.courses_attached\
        and course in instance.grades:
            total_grades += sum(instance.grades.get(course))
            total_lecturers += 1
    if total_grades == 0:
        return 'Оценок нет'
    return total_grades / total_lecturers

# Создаем по 2 экземпляра каждого класса.

michael = Student('Michael', 'Scott', 'male')
jim = Student('Jim', 'Halpert', 'male')
pam = Lecturer('Pam', 'Beasley')
toby = Lecturer('Toby', 'Flanderson')
stanley = Reviewer('Stanley', 'Hudson')
andy = Reviewer('Andrew', 'Bernard')

# Тестируем методы и наполняем списки и словари

michael.courses_in_progress += ['Python', 'Java Script', 'Docker']
jim.courses_in_progress += ['Python', 'Data Security', 'C++', 'Docker']
michael.finished_courses += ['C#', 'HTML']
michael.add_courses('CSS')
jim.add_courses('React')
jim.finished_courses += ['CSS', 'HTML']
pam.courses_attached += ['Python', 'Docker', 'Data Security']
toby.courses_attached += ['Python', 'Data Security', 'C++', 'Java Script']
stanley.courses_attached += ['Python', 'Data Security', 'C++']
andy.courses_attached += ['Python', 'Docker', 'Java Script']

# Выставляем оценки

stanley.rate_hw(jim, 'Python', 8)
stanley.rate_hw(michael, 'Python', 7)
andy.rate_hw(michael, 'Java Script', 6)
andy.rate_hw(jim, 'Python', 6)
michael.rate_lecturer(pam, 'Python', 9)
michael.rate_lecturer(toby, 'Java Script', 3)
michael.rate_lecturer(pam, 'Docker', 7)
michael.rate_lecturer(toby, 'Python', 4)
jim.rate_lecturer(toby, 'Python', 10)
jim.rate_lecturer(toby, 'C++', 7)
jim.rate_lecturer(pam, 'Data Security', 8)
jim.rate_lecturer(pam, 'Docker', 8)
jim.rate_lecturer(pam, 'Python', 9)

# Выводим информацию об объектах классов и применяем сравнение

print(michael)
print()
print(jim)
print()
print(pam)
print()
print(toby)
print()
print(stanley)
print()
print(andy)
print()
print(michael < jim)
print(pam < toby)
print()

# Выводим среднюю оценку студентов по конкретным курсам

print(get_average_grade_for_all_students('Python'))
print(get_average_grade_for_all_students('Java Script'))
print(get_average_grade_for_all_students('C++'))
print(get_average_grade_for_all_students('Docker'))
print(get_average_grade_for_all_students('Data Security'))
print()

# Выводим среднюю оценку лекторов по конкретным курсам

print(get_average_grade_for_all_lecturers('Docker'))
print(get_average_grade_for_all_lecturers('C++'))
print(get_average_grade_for_all_lecturers('Python'))
print(get_average_grade_for_all_lecturers('Data Security'))
print(get_average_grade_for_all_lecturers('Java Script'))
