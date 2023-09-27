class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# метод для вычисления средней оценки
    def calc_average(self):  
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = round(sum(grades) / len(grades), 2)
        return average_grade   
    
#метод выставления оценок Лекторам Студентами   
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка' 
# метод для изменения информации об экземпляре класса    
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.calc_average()} \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} \nЗавершенные курсы: {', '.join(self.finished_courses)}"

# метод для сравнивания по средней оценке
    def __lt__(self, students):
        if not isinstance(students, Student):
            print('Такого лектора нет')
            return
        return self.calc_average() < students.calc_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# добавлен класс Лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # добавлен атрибут с оценками для Лектора от Студентов
        self.grades = {} 

# метод для вычисления средней оценки    
    def calc_average(self):  
        grades = []
        for grade in self.grades.values():
            grades += grade
        average_grade = round(sum(grades) / len(grades), 2)
        return average_grade    
         
# метод для изменения информации об экземпляре класса  
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.calc_average()}'
        
# метод для сравнивания по средней оценке
    def __lt__(self, lectors):
        if not isinstance(lectors, Lecturer):
            print('Такого лектора нет')
            return
        return self.calc_average() < lectors.calc_average()

# добавлен класс Проверяющие
class Reviewer(Mentor):
    # def __init__(self, name, surname):
    #     super().__init__(name, surname)
    pass

# теперь оценки студентам могут ставить только проверяющие, т.к. это уникальный для класса метод
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка' 
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"
        
cool_rewiewer_1 = Reviewer('Nancy', 'Bosh') 
cool_rewiewer_1.courses_attached += ['Python', 'Git']

cool_rewiewer_2 = Reviewer('James', 'Gorby') 
cool_rewiewer_2.courses_attached += ['Python', 'Java']

best_student_1 = Student('Ruoy', 'Eman', 'F')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.finished_courses += ['Введение в программирование']

best_student_2 = Student('Boby', 'Rick', 'M')
best_student_2.courses_in_progress += ['Python', 'Java']

cool_lector_1 = Lecturer('Lucy', 'Jo')
cool_lector_1.courses_attached += ['C++', 'Python', 'Java']

cool_lector_2 = Lecturer('Bri', 'Hadson')
cool_lector_2.courses_attached += ['Java', 'Python']

cool_rewiewer_1.rate_hw(best_student_1, 'Python', 10)
cool_rewiewer_1.rate_hw(best_student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(best_student_1, 'Git', 9)
cool_rewiewer_1.rate_hw(best_student_1, 'Java', 9)

cool_rewiewer_2.rate_hw(best_student_2, 'Python', 10)
cool_rewiewer_2.rate_hw(best_student_2, 'Python', 5)
cool_rewiewer_2.rate_hw(best_student_2, 'C++', 10)
cool_rewiewer_2.rate_hw(best_student_2, 'Java', 9)

best_student_1.rate_hw(cool_lector_1, 'C++', 5)
best_student_1.rate_hw(cool_lector_1, 'Python', 10)
best_student_1.rate_hw(cool_lector_1, 'Python', 10)

best_student_2.rate_hw(cool_lector_2, 'Python', 15)
best_student_2.rate_hw(cool_lector_2, 'Python', 15)

print(cool_lector_1 > cool_lector_2)
print(cool_lector_1 < cool_lector_2)
print(best_student_2 > best_student_1)
print(best_student_2 < best_student_1)

print(best_student_1)
print(best_student_2)

print(cool_rewiewer_1)
print(cool_rewiewer_2)

print(cool_lector_1)
print(cool_lector_2)

student_list = [best_student_1, best_student_2]
lector_list = [cool_lector_1, cool_lector_2]

#  функция для вычисления средней оценки по курсу
def grades_students(student_list, course):
    over_student_rating = 0
    i = 0
    for listener in student_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            over_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += over_student_rating
            i += 1
    if over_student_rating == 0:
        return f'Оценок по этому курсу нет'
    else:
        return f'{over_student_rating / i}'


def grades_lecturers(lector_list, course):
    average_rating = 0
    i = 0
    for lecturer in lector_list:
        if course in lecturer.grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.grades[course])
            average_rating += overall_lecturer_average_rates
            i += 1
    if average_rating == 0:
        return f'Оценок по этому курсу нет'
    else:
        return f'{average_rating / i}'

print(f'Средняя оценка студентов по курсу "Git": {grades_students(student_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(student_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(student_list, "Python")}')
print(f'Средняя оценка студентов по курсу "С++": {grades_students(student_list, "С++")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lector_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lector_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lector_list, "Python")}')
print(f'Средняя оценка лекторов по курсу "С++": {grades_lecturers(lector_list, "С++")}')
