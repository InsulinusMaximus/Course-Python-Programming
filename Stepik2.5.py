#1
'''
Списки (массивы): 
к ним применимы те же индексные операции, что и к срокам
Сложение:
array1=[1,2,3] +  array2=[4,5] == [1,2,3,4,5]
Умножение:
array1=[1,2,3]*2 == [1,2,3,1,2,3]

В списках поиндексно можно заменять элементы:
array1=[1,2,3]
array1[0]=2 -->
array1=[2,2,3]

Метод append (перевод: добавить) добавляет в конец спика элемент:
array1.append(9)
array1=[1,2,3,9]
То же самое делает +=:
array+=[7]
array1=[1,2,3,9,7]

Метод insert (перевод: вставлять) вставляет по указанному индексу значение сдвигая прежние вправо:
array1=[1,2,3]
array1.insert(1,9)
array1=[1,9,2,3]

'''
'''
students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(len(students))
'''
'''
Для удаления моно использовать:
array=[1,2,3,4,5,3]
array.remove(3)
array=[1,2,4,5,3]
Или по индексу:
array=[1,2,3,4,5]
del array[0]
array=[2,3,4,5]

Для проверки значния элемента в списке используется in:
if '2' in students:
    print ('yes, it here')
elif '2' not in students:
    print('noooot')

Для нахождения индекса искомого элемента используется index:
array=[1,2,3,4,5,3]
ind=array.index('1') --> 0

Отсортировать список можно с помощью функции sorted() (не изменяет сам список) или метода .sort (изменяет сам список), для возвращения 
максимального или минимального значения можно использовать функции min(), max()
Однико для применения этих функций элементы списка должны быть сравнимы!

Для получения списка в обратном порядке можно исп. ф-цию reversed() (не изменяет сам список) или метод .revers (изменяет сам список)
Также можно исп.:
array[::-1] (тоже спитсон не изменится а лишь вернется)

При присвоении какой-то переменной значения array=[1,2,3], создается объект в памяти [1,2,3], при присвоении новой переменной
значнения старой arraynew=array новая переменная в памяти сошлется на тот же объект, а не создаст новый.
Таким образом, изменяя значение первой переменной, изменится и значение новой:
array[0]=9
array=[9,2,3]
arraynew=[9,2,3]

'''
'''
a = [1 , 2 , 3 ]
b = a
# значения списка b?
print(b, end='')

a[1] = 10
# значения списка b?
print(b, end='')

b[0] = 20
# значения списка a?
print(a, end='')

a = [5, 6]
# значения списка b?
print(b, end='')
'''
'''
Для ввода списка используется следующая конструкция:
list=[int(i) for i in input().split()]
Также заполнить список можно:
list=[i for i in range(5)]
list=[0 for i in range(5)]

'''
#2
'''
list=[int(i) for i in input().split()]
sum=0
for i in range(len(list)):
    sum+=list[i]
print(sum)
'''
#3
'''
list=[int(i) for i in input().split()]
newlist=[]

if len(list)==1:
    print(list[0])
else:
    for i in range(len(list)):
        if i == 0:
            newlist.append(list[1]+list[-1])
        elif i== len(list)-1:
            newlist.append(list[0]+list[-2])
        else:
            newlist.append(list[i+1]+list[i-1])
    for j in range(len(newlist)):
        if j==len(newlist):
            print(newlist[j])
        else:
            print(newlist[j], end=" ")
'''
#4

list=[int(l) for l in input().split()]
newlist=[]

list.sort()

for i in range(len(list)):
    if i!=len(list)-1:
        if list[i]==list[i+1] and list[i] not in newlist:
            newlist.append(list[i])

for j in range(len(newlist)):
        if j==len(newlist):
            print(newlist[j])
        else:
            print(newlist[j], end=" ")

'''
В Python существует возможность генерации многомерных списков:
a=[[1, 2, 3][4, 5, 6][7, 8, 9]]
Тогда индексация происходит следующим образом:
a[1] == [4, 5, 6]
a[1][1] == [5]

Сгенерировать сногомерный список можно:
a=[[0]*n for n in range(n)]
a=[[0 for j in range(n)] for i in range(n)]

'''

