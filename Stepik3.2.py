'''
Множества - позволяют хранить много элементов данных

set() # создание пустого множества

, узнать содержание которых можно:

s in set # false

Записать данные в множества можно:

set={1,1,1,1}

Операции с множествами:

set.add() # добавляет в множество переданный параметр, если значение уже было, то ничего не изменится
set.remove() # удаление элемента из множества, если его нет то выйдет ошибка
set.discard() # удаляет элемент даже если его нет, т е не выдает ошибку
set.clear() # очищает множество

len(set) #  количество элементов

set={'a', 'b', 'c', 'd', 'a'}

for i in set:
    print(x) # вывод: b, d, c, a -- т е порядок сохранен не будет, кроме того повторяющиеся элементы будут выведены один раз



Словари - ассоциативный массив, позволяющий хранить данные в паре ключ-значение

dict a or a={} # синтаксис вызова словаря

a={'key':123, 'key1':000} # где key-ключ,а 123-значение 

Операции со словарями:

key in a #
key not in a

a[key]=value #присваение ключу значение
a[key] # если такого ключа нет, вернется ошибка

a.get[key] # полученное значение - 123 , если значени отсутствует вернется none

del a[key] # по этому ключу будет удалена пара - и значение и ключ

Ключами в словарях не могут быть изменяемые элементы (списки, словари, множества)

Конструкции перебора элементов в словарях:

d = {'a': 127, 'b': 128, 'c': 130}

for key in d:
    print(key, end'') # a b c

for key in d.keys():
    print(key, end'') # a b c

for value in d.values():
    print(value, end'') # 127 128 130

for key, value in d.items():
    print(key, value, end'') # 127 128 130

В словарях в качестве значения ключей можно передовать список значенийб, тогда по оному ключу будет храниться список значений
'''
#1
'''
def update_dictionary(d, key, value):
 
    if key in d:
         d[key].append(value)
    elif key*2 in d:
         d[key*2].append(value)
    else:
        d.update({key*2 : [value]})

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''

#2
'''
s = input().lower().split()
d={}

for i in s:
    c=s.count(i)
    d[i]=c

for key, value in d.items():
    print(key, value, end='\n')
'''
#3
'''
n=int(input())
i=0
x={}
while i!=n:
    s=int(input())
    if s not in x:
        x.update({s : f(s)})
        print(x[s])
    else:
        print(x[s])
    i+=1
'''