#1
'''
a=int (input ())
b=int (input ())
c=int (input ())
d=int (input ())

for i in range(a-1,b+1):
    for j in range(c,d+1):
        if i==a-1:
            if j==c:
                print(" ",j,end=' ')
            else:
                print(j,end=' ')
        elif j==c:
            print(i,i*j,end=' ')
        else:
            print(i*j,end=' ')
    print()
'''
#2
'''
Если значения вводятся с в одну строку, но с разделением (например, пробел), тогда с помощью функции split()
(перевод: расщепление, раскол) можно раделить получившееся строковое значение на неколько в местах разделения. 
Для того чтобы применить функцию split() к функции input() необходимо использовать контрукцию: input().split().
Тогда общей вид чтения вводных данных будет: 

a,b = input().split()

Однако такие данные будут приняты в качестве строкового значения и в случае необходимости использования их 
в качестве другого типа данных необходимо применить соответствующую функцию (например, int(a), int(b)).
Но в случае приема большого числа данных или просто необходимости более лаканичного решения можно использовать
конструкцию:

a,b=(int(i) for i in input().split())

'''
a=int (input ())
b=int (input ())
s=0
j=0

for i in range(a,b+1):
    if i%3==0:
        s+=i
        j+=1
print(s/j)
