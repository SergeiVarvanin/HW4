"""Практическая работа №1
Написать программу на Python, которая:
Подсчитывает общее количество символов в файле
Подсчитывает общее количество символов без пробелов
Подсчитывает количество символов без знаков препинания
Подсчитывает количество слов в файле
Подсчитывает количество предложений
Результат подсчета должен быть выведен в консоль"""


import re


# Количество символов в файле
symbols = 0
# Количество символов без пробелов
swpro = 0
# Количество символов без знаков препинания
swpun = 0
# Количество слов в файле
words = 0
# Количество предложений
offers = 0
# Просто переменная)
i = 0

with open("aristotle.txt", "rt") as text:
    data = text.read()
    symbols = len(data)
    swpro = symbols - data.count(' ')
    swpun = len(re.sub(r'[^\w\s]', '', data))
    words = len(re.split(r'[,\s]\s*', data))
    offers = len(re.sub(r'[.!?]\s', r'|', data).split('|'))


print('Количество символов в тексте: ', symbols)
print('Количество символов в тексте без пробелов: ', swpro)
print('Количество символов в тексте без знаков препинания: ', swpun)
print('Количество слов в тексте: ', words)
print('В этом тексте {} предложения.'.format(offers))
