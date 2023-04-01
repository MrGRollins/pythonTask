# 1. Написать функцию, которая проверяет является ли строка палиндромом.

# начальные данные:
string = "abccаa"

reverse_string = "".join(reversed(string))

# Проверка на палиндром
if (string == reverse_string):
    print("Строка:", reverse_string, '- палиндромом')
else:
    print("Строка:", reverse_string, '- НЕ палиндромом')