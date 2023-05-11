# 1. Написать функцию, которая проверяет является ли строка палиндромом.

# Начальные данные:
string = "abcccc"

# Функция проверки на полиндром
def polindrom_checker():
    reverse_string = "".join(reversed(string))

    # Проверка на палиндром
    if string == reverse_string:
        return True

if __name__ == '__main__':
    if polindrom_checker() == True:
        print("Строка:", string, '- палиндромом')
    else:
        print("Строка:", string, '- НЕ палиндромом')