# 4.	Создать классы студент, аспирант. Студент содержит свойства: номер группы, средний балл.
#       Аспирант отличается от студента наличием научной работы (название работы в виде строки).
#       Реализовать в классах следующие методы:
#       •	вывести информацию (фио, возраст)
#       •	вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента,
#           если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р.
#       •	Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше).

class Student:
    STIPEND = 0
    STIPEND_GOOD = 4000
    STIPEND_EXCELLENT = 6000

    AVG_THREE = 3
    AVG_GODD = 4
    AVG_EXCELLENT = 5

    def __init__(self, first_name, last_name, age_student, groups_student, avg_rating_student):

        self.first_name = first_name
        self.last_name = last_name
        self.age_student = age_student
        self.groups_student = groups_student
        self.avg_rating_student = avg_rating_student

    @property
    def student_info(self):
        print(f"{self.first_name}{' '}{self.last_name}{', '}{self.age_student}{' age'}")

    @property
    def stipends_calculating(self):

        if self.avg_rating_student == self.AVG_EXCELLENT:
            self.stipends = self.STIPEND_EXCELLENT
        elif self.avg_rating_student >= self.AVG_THREE and self.avg_rating_student < self.AVG_EXCELLENT:
            self.stipends = self.STIPEND_GOOD
        else:
            self.stipends = self.STIPEND
        return self.stipends

    @property
    def compares_stipends(self, other):
        if self.stipends > other.stipends:
            self.max_stipends_student = self.first_name
        else:
            self.max_stipends_student = other.first_name
        return self.max_stipends_student

class PostGraduate:
    STIPEND = 0
    STIPEND_GOOD = 6000
    STIPEND_EXCELLENT = 8000

    AVG_THREE = 3
    AVG_GODD = 4
    AVG_EXCELLENT = 5

    def __init__(self, first_name, last_name, age_student, groups_student, title_scientific_work, avg_rating_student):
        self.first_name = first_name
        self.last_name = last_name
        self.age_student = age_student
        self.groups_student = groups_student
        self.title_scientific_work = title_scientific_work
        self.avg_rating_student = avg_rating_student

    @property
    def student_info(self):
            print(f"{self.first_name}{' '}{self.last_name}{', '}{self.age_student}{' age'}")

    @property
    def stipends_calculating(self):

        if self.avg_rating_student == self.AVG_EXCELLENT:
            self.stipends = self.STIPEND_EXCELLENT
        elif self.avg_rating_student >= self.AVG_THREE and self.avg_rating_student < self.AVG_EXCELLENT:
            self.stipends = self.STIPEND_GOOD
        else:
            self.stipends = self.STIPEND
        return self.stipends

    @property
    def compares_stipends(self, other):
        if self.stipends > other.stipends:
            self.max_stipends_student = self.first_name
        else:
            self.max_stipends_student = other.first_name
        return self.max_stipends_student

if __name__ == '__main__':
    student1 = Student("Ivan", "Pavlov", 18, "3542/8", 4.3)
    student2 = Student("Roman", "Ivanov", 20, "3542/7", 5)
    postGraduate = PostGraduate("Alexey ", "Ropas ", 22, " 4572/1", "Collector", 4)

    print(student1.student_info, " | ", "Стипендия студента: ", student1.stipends_calculating)
    print(student2.student_info, " | ", "Стипендия студента: ", student2.stipends_calculating)
    #print(postGraduate.postGraduate_info, " | ", postGraduate.calculating_stipends)






