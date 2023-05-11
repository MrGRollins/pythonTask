# 4.	Создать классы студент, аспирант. Студент содержит свойства: номер группы, средний балл.
#       Аспирант отличается от студента наличием научной работы (название работы в виде строки).
#       Реализовать в классах следующие методы:
#       •	вывести информацию (фио, возраст)
#       •	вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента,
#           если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р.
#       •	Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше).

class Student:
    def __init__(self, name_Student, last_name_Student, age_Student, groups_Student, avg_rating_Student):

        self.name_Student = name_Student
        self.last_name_Student = last_name_Student
        self.age_Student = age_Student
        self.groups_Student = groups_Student
        self.avg_rating_Student = avg_rating_Student

    @property
    def student_info(self):
        print(f"{self.name_Student}{' '}{self.last_name_Student}{', '}{self.age_Student}{' age'}")

    @property
    def calculating_stipends(self):
        self.stipends_st = 0

        if self.avg_rating_Student == 5:
            self.stipends_st = 6000
        elif self.avg_rating_Student >= 3 and self.avg_rating_Student < 5:
            self.stipends_st = 4000
        else:
            self.stipends_st = 0

        print("Размер стипендии студента:", self.stipends_st)

    def stipends_delta_calculating(self, other):
        if self.self.stipends_st > other.stipends:
            print ("Стипендия ", self.name_Student, "больше чем у ", other.name_Student)
        else:
            print("Стипендия ", other.name_Student, "больше чем у ", self.name_Student)


class PostGraduate:
    def __init__(self, name_PostG, last_name_PostG, age_PostG, groups_PostG, scientific_work_PostG, avg_rating_PostG):
        self.name_PostG = name_PostG
        self.last_name_PostG = last_name_PostG
        self.age_PostG = age_PostG
        self.groups_PostG = groups_PostG
        self.scientific_work_PostG = scientific_work_PostG
        self.avg_rating_PostG = avg_rating_PostG

    @property
    def postGraduate_info(self):
            print(f"{self.name_PostG}{' '}{self.last_name_PostG}{', '}{self.age_PostG}{' age'}")

    @property
    def calculating_stipends(self):
        self.stipends = 0

        if self.avg_rating_PostG == 5:
            stipends = 8000
        elif self.avg_rating_PostG >= 3 and self.avg_rating_PostG < 5:
            stipends = 6000
        else:
            stipends = 0

        print("Размер стипендии аспиратна:", stipends)

    def stipends_delta_calculating(self, other):
        if self.stipends > other.stipends:
            print ("Стипендия ", self.name_PostG, "больше чем у ", other.name_PostG)
        else:
            print("Стипендия ", other.name_PostG, "больше чем у ", self.name_PostG)

if __name__ == '__main__':
    student1 = Student("Ivan", "Pavlov", 18, "3542/8", 4.3)
    student2 = Student("Roman", "Ivanov", 20, "3542/7", 5)
    postGraduate = PostGraduate("Alexey ", "Ropas ", 22, " 4572/1", "Collector", 4)

    print(student1.student_info, " | ", student1.calculating_stipends)
    print(student2.student_info, " | ", student2.calculating_stipends)
    #print(postGraduate.postGraduate_info, " | ", postGraduate.calculating_stipends)







