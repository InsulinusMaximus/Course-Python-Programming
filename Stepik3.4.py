'''
Чтение файла:

Для чтения пользовательского ввода в файле используются следующие конструкции:

inf = open('file.txt', 'r') 
s1 = inf.readline()
s2 = inf.readline()
inf.close()

or

with open('text.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

s=inf.readline().strip() # убирает служебные символы типа '\n'


import os
os.path.join('.', 'dirname', 'filename.txt') # создает путь к файлу

Построчное чтение файла:

with open('input.txt') as inf:
    for line in inf:
        line=line.strip()
        print(line)
'''
'''
with open('input.txt', 'r') as inf:
    for line in inf:
        line=line.strip()
        print(line)
'''
'''
Запись в файл:

ouf = open('file.txt', 'w') 
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

or

with open('input.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))

'''
#1
'''
inf = open('dataset_3363_2.txt', 'r') 
s = inf.readline()
inf.close()

file_out=open('return3.4_1.txt', 'w')

for i in range(len(s)):
    if s[i].isdigit()==True:

        if s[i+1].isdigit()==True:
            news=int(s[i]+s[i+1]) 
            out=s[i-1]*news
            file_out.write(out) 
        elif s[i-1].isalpha()==True and s[i+1].isalpha()==True :
            news=int(s[i])
            out=s[i-1]*news
            file_out.write(out)

file_out.close()
'''
#2
'''
s=''
inf = open('dataset_3363_3.txt', 'r') 
d={}
for line in inf.readlines():
    for word in line.split():
        if word not in d:
            num=1
            d.update({word : num})
        elif word in d:
            num=d.get(word)+1
            d[word]=num
inf.close()            


r=[]
maximum=max(sorted(d.values()))
for key in d.keys():
    if d[key]==maximum:
        r.append(key)
itog=''
if len(r)==1:
    min=r[0]
    print(1)
else:
     for i in range(len(r)-1):
        if i==len(r):
            min=r[i]
        elif r[i]<r[i+1]:
            min=r[i]
        else:
            min=r[i+1]
min=str(min)
value=str(d[min])
itog=min+' '+value


file_out=open('return3.4_2.txt', 'w')
file_out.write(itog)
file_out.close()
'''
# 3

inf = open('dataset_3363_4.txt', 'r') 
d = []
matem = countmatem = fisic = countfisic = russ = countruss = 0

for line in inf.readlines():
    count = 0
    sum = 0
    for word in line.split(';'):
        #print(word)
        if count != 0:
            word = int(word)
            sum += word

            if count == 1:
                matem += word
                countmatem+=1

            elif count == 2:
                fisic += word
                countfisic+=1

            elif count == 3:
                russ += word
                countruss+=1

        count += 1
    d.append(sum/3)
#print(*d)

meanmatem=matem/countmatem
meanfisic=fisic/countfisic
meanruss=russ/countruss
meanmatem=str(meanmatem)
meanfisic=str(meanfisic)
meanruss=str(meanruss)

file_out = open('return3.4_3.txt', 'w')

for i in d:
    i=str(i)
    file_out.write(i)
    file_out.write('\n')
file_out.write(meanmatem)
file_out.write(' ')
file_out.write(meanfisic)
file_out.write(' ')
file_out.write(meanruss)
file_out.close()          


