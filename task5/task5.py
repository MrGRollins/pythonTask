# 5. Реализовать декоратор, который выводит в консоль время выполнения декорируемой функции.
#    Протестировать работу декоратора на двух функциях:
#    •	Функция вычисляет сумму двух чисел a и b, выводит результат в консоль
#    •	Функция читает из файла input.txt значение двух чисел a и b, записывает результат вычисления
#       в файл output.txt (файлы приложить к репозиторию)

import time

def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Время декорируемой функции  - {func.__name__}():", round((end_time - start_time) * 10**3, 3), "ms")

        return result
    return wrapper

@check_time
def sum(a: float, b: float):
    return a + b

@check_time
def read_file(input_file: str, output_file: str):
    try:
        sum = 0

        with open("input.txt", "r") as input_file:
            a = float(input_file.readline())
            b = float(input_file.readline())
            sum = a + b
        with open("output.txt", "w") as output_file:
            output_file.write(str(sum))
        return sum

    except (FileExistsError, FileNotFoundError) as error:
        print(error)

if __name__ == '__main__':
    print(sum(4.5, 7.1))
    print(read_file("input.txt", "output.txt"))