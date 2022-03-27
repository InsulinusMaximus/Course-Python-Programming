#1
'''
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)

#2

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

#3
x=1
y=0
while x!=0:
    x=int(input())
    y+=x
print(y)

#4

a=int(input ())
b=int(input ())
d=a

while a%b!=0:
    a=a+d
print(a)
'''
#5
x=1
while x<1000:
    x=int(input ())
    if x<10:
        continue
    elif x>100:
        break
    else:
        print(x)



