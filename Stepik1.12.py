#1 -- Программа для вычисления площади S треугольника по трем сторонам a, b, c
'''
a=int(input ())
b=int(input ())
c=int(input ())

p=((a+b+c)/2)
S=(p*(p-a)*(p-b)*(p-c))**(0.5)
print(S)

#2 -- (−15,12]∪(14,17)∪[19,+∞)

x=int(input ())

if -15<x<=12 or 14<x<17 or x>=19:
    print(True)
else:
    print(False)

#3 -- Калькулятор

x=float(input())
y=float(input())
o=str(input())

if o == "+":
    print (x+y)
elif o == "-":
    print (x-y)
elif o == "/":
    if y==0:
        print("Деление на 0!")
    else:
        print (x/y)
elif o == "*":
    print (x*y)
elif o == "mod":
    if y==0:
        print("Деление на 0!")
    else:
        print (x%y)
elif o == "pow":
    print (x**y)
elif o == "div":
    if y==0:
        print("Деление на 0!")
    else:
        print (x//y)

#4 -- Площади фигур

fig = str(input())

if fig=="треугольник":
    a=int(input())
    b=int(input())
    c=int(input())

    p=((a+b+c)/2)
    S=(p*(p-a)*(p-b)*(p-c))**(0.5)
    print(S)
elif fig=="прямоугольник":
    a=int(input())
    b=int(input())

    S=a*b
    print(S)
elif fig=="круг":
    r=int(input())
    pi=3.14

    S=pi*r**2
    print(S)

#5 -- Сортировка трех чисел

x=int (input())
y=int (input())
z=int (input())

array = [x,y,z]
array=sorted(array)
       
min=array[0]
mid=array[1]
max=array[2]

print(" ")
print (max)
print (min)
print (mid)

#6 -- Программист - программистов - программиста

x=str(input())
d=len(x)
num=x[d-1]
numb=x[d-2]
dec=numb+num

if num=='0' or '4'<num<='9' or (dec=='11' and d>1) or dec=='12' or dec=='13' or dec=='14' or dec=='15' or dec=='16' or dec=='17' or dec=='18' or dec=='19' :
       print("{} программистов".format(x))
elif num=='1':
    print("{} программист".format(x))
elif '1'<num<'5':
    print("{} программиста".format(x))

#6.1 -- Самый короткий вариант (программист - программистов - программиста)
n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))
'''
#7 -- Счастливый билет

x=str(input())
d=len(x)
left=int(x[d-1])+int(x[d-2])+int(x[d-3])
right=int(x[d-4])+int(x[d-5])+int(x[d-6])

if left==right:
    print('Счастливый')
else:
    print('Обычный') 