#1
'''
В Python строки могут быть перебраны по индексу как массив:

x='abCDfg' p='c'
x[0]=='a'
x[-1]=='g'

Существует масса методов строк:

x.upper() -> 'ABCDFG'
x.lower() -> 'abcdfg'
x.count(c) -> 1 -- возвращает количество указанного в скобках символа в приведенной строке
x.found(p) -> 2 -- возвращает индекс общего значения в двух переменных (если искомое значение отсутствует, тогда возвращается -1)
    *Данную функцию также можно реализовать через условие:
    if 'c' in x:
x.replace('C', 'c') -> 'abcDfg' -- заменяет все 'C' на 'c' 

'''
'''
x=input()
count=0

for i in x:
    count+=1
c=x.count('c')
C=x.count('C')
g=x.count('g')
G=x.count('G')

print((c+C+g+G)/count*100)'''

#2

'''
В Python строки можно перебирать и изменять по индексно:

x='abcdefg'

x[1]=='b'
x[1:4]=='bcd'
x[:4]=='abcd'
x[4:]=='efg'
x[-4:]=='defg'
x[1:-1]=='bcdef'
x[1:-1:2]=='be'
x[::-1]=='gfedcba' --> Символы в обратном порядке


#2.1
s = 'abcdefghijk'
print(s[3:6], s[:6], s[3:], s[::-1], s[-3:], s[:-6], s[-1:-10:-2])
'''
#2.2

x=input()
count=1

for i in range(len(x)-1):
    if x[i] == x[i+1]:
        count+=1
    elif x[i]!=x[i+1]:
        print(x[i], end='')
        print(count, end='')
        count=1
print(x[-1], end='')
print(count, end='')  