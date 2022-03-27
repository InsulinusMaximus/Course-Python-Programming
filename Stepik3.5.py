'''
Для импорта моделя необходимо указать:
import my_module.py
Для использования функций, находящихся в модуле необходимо после объявления импорта указывать:
my_module.function()
Если необходимо импортировать не весь модуль, а только конкретную функцию тогда:
from my_module import function()
Также можно присвоить импортируемой функции собственное имя:
from my_module import function() as my_function()
my_function()
Импортировать все функции можно:
from my_module import*

Стандартная библиотека:

Модуль 'sys' содержит функцию списка аргументов командной строки 'argv':
import sys
print(len(sys.argv)) # подсчитывает количество аргументов переданных конмандной строкой при запуске программы

Модуль 'subprocess' позволяет вызывать внешние процессы, например программы внутрь своей программы
subprocess.call("<название программы>", "<куда вывести ("-h" - выведет в консоль результат запущенной программы)>")

'''
#1
'''
import math

radius = float(input())

def circle_perimeter(r):
    perimeter = 2*r*math.pi
    return perimeter

print(circle_perimeter(radius))
'''
#2
'''
import sys
list = sys.argv
for i in range(1,len(list)):
    print(list[i])
'''




