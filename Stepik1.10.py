#1
'''
a=int(input ())
b=int(input ())
h=int(input ())

if h <= b and h >= a:
    print ('Это нормально')
elif h < a:
    print ('Недосып')
else:
    print ('Пересып')
'''
#2

x=int(input ())

if ((x%4==0 and (not x%100==0)) or x%400==0):
    print ('Високосный')
else:
    print ('Обычный')
