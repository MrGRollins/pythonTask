# 2.Написать функцию, которая принимает два аргумента: лямбда функция для фильтрации массива, массив строк.
#   Сделать вызов данной функции для следующих функций фильтрации:
#   •	Исключить строки с пробелами
#   •	Исключить строки, начинающиеся с буквы “a”
#   •	Исключить строки, длина которых меньше 5

from collections.abc import Callable
from typing import List
from functools import reduce

def data_cleaning_single_filter(
        filter_function: Callable[str, bool],
        list_for_filtering: List[str]) -> List[str]:
    return list(filter(filter_function, list_for_filtering))

def data_cleaning_via_filters_apart(
        filters_list: List[Callable[str, bool]],
        list_for_filtering: List[str]) -> List[List[str]]:
    return list(map(lambda filter_fun: data_cleaning_single_filter(filter_fun, list_for_filtering), filters_list))

def data_cleaning_via_filters_together(
        filters_list: List[Callable[str, bool]],
        list_for_filtering: List[str]) -> List[str]:
    raw_lists = data_cleaning_via_filters_apart(filters_list, list_for_filtering)
    return list(reduce(lambda list_1, list_2: set(list_1) & set(list_2), raw_lists))

filter_list = [
    lambda line: not line.find(" ") != -1,
    lambda line: not line.startswith("a"),
    lambda line: not len(line) < 5
]

if __name__ == '__main__':
    test_lines = [
        "Test",
        "Интервьюер интервента интервьюировал",
        "Hello world!",
        "тенис",
        "vibe"
    ]

    print(test_lines)
    test_lines = data_cleaning_via_filters_apart([lambda line: not line.find(" ") != -1], test_lines)[0]
    print(test_lines)
    test_lines = data_cleaning_via_filters_apart([lambda line: not line.startswith("a")], test_lines)[0]
    print(test_lines)
    test_lines = data_cleaning_via_filters_apart([lambda line: not len(line) < 5], test_lines)[0]
    print(test_lines)
    test_lines = [
        "Test",
        "Интервьюер интервента интервьюировал",
        "Hello world!",
        "тенис",
        "vibe"
    ]

    test_lines = data_cleaning_via_filters_together(filter_list, test_lines)
    print(test_lines)