#1
'''
suma=0
sqrt=0

while True:
    num=int(input())
    suma+=num
    sqrt+=num**2
    if suma==0:
        break
print(sqrt)
'''
#2
'''
num=int(input())
list = [[i]*i for i in range(num+1)]
newlist=[]
for i in list:
    for j in i:
        newlist.append(j)

for i in newlist[:num]:
    print(i, end=" ")
'''
#3
'''
lst=[int(i) for i in input().split()]
x=int(input())
ind=[]
for i in range(len(lst)):
    if lst[i]==x:
        ind.append(i)
if len(ind)==0:
    print('Отсутствует')
else:
    for i in ind:
        print(i, end=" ")

#4

str=''
list=[]

while True:
    str=input()
    if str!='end':
        str=str.split()
        for i in range(len(str)):
            str[i]=int(str[i])
        list.append(str)
    else:
        break
# Проверка по условию ввода: матрица 1X1 (M1)
if len(list)==1 and len(list[0])==1:
    M1=list[0][0]
    print(M1*4)
# Проверка по условию ввода: матрица 1X... (M2)
elif len(list)==1:
    for i in range(len(list)):
        indstolb=i
        for j in range(len(list[i])):
            indstroki=j
            if indstroki==len(list[i])-1:
                M2=list[indstolb][indstroki]+list[indstolb][indstroki]+list[indstolb][indstroki-1]+list[indstolb][0]
                print(M2,end=' ')
            else:
                M2=list[indstolb][indstroki]+list[indstolb][indstroki]+list[indstolb][indstroki-1]+list[indstolb][indstroki+1]
                print(M2,end=' ')
# Проверка по условию ввода: матрица ...X1 (M3)
elif len(list[0])==1:
    for i in range(len(list)):
        indstolb=i
        for j in range(len(list[i])):
            indstroki=j
            if indstolb==len(list)-1:
                M3=list[indstolb-1][indstroki]+list[0][indstroki]+list[indstolb][indstroki]+list[indstolb][indstroki]
                print(M3,end=' ')
            else:
                M3=list[indstolb-1][indstroki]+list[indstolb+1][indstroki]+list[indstolb][indstroki]+list[indstolb][indstroki]
                print(M3,end=' ')
        print(end ="\n")
# Проверка по условию ввода: матрица ...X... (M4)
else:
    for i in range(len(list)):
        indstolb=i
        for j in range(len(list[i])):
            indstroki=j
            if indstolb==len(list)-1 and indstroki==len(list[i])-1:
                M4_1=list[indstolb-1][indstroki]+list[0][indstroki]+list[indstolb][indstroki-1]+list[indstolb][0]
                print(M4_1,end=' ')

            elif indstolb==len(list)-1:
                M4_2=list[indstolb-1][indstroki]+list[0][indstroki]+list[indstolb][indstroki-1]+list[indstolb][indstroki+1]
                print(M4_2,end=' ')
                
            elif indstroki==len(list[i])-1:
                M4_3=list[indstolb-1][indstroki]+list[indstolb+1][indstroki]+list[indstolb][indstroki-1]+list[indstolb][0]
                print(M4_3,end=' ')

            else:
                M4_4=list[indstolb-1][indstroki]+list[indstolb+1][indstroki]+list[indstolb][indstroki-1]+list[indstolb][indstroki+1]
                print(M4_4,end=' ')
        print(end ="\n")
'''
#5

n=int(input())

list=[[0]*n for _ in range(n)]
list[0]=[(col+1) for col in range(n)]

index=n
y=0; x=n-1; r=n

while index<n**2:
    r-=1
    for _ in range(r): # вертикаль по направлению вниз
        y+=1
        index+=1; list[y][x]=index
    for _ in range(r): # горизонталь по направлению влево
        x-=1
        index+=1; list[y][x]=index 
    if index>=n**2:
        break    
    r-=1
    
    for _ in range(r): # вертикаль по направлению вверх
        y-=1
        index+=1; list[y][x]=index
    for _ in range(r): # горизонталь по направлению вправо
        x+=1
        index+=1; list[y][x]=index

for i in list:
    print('\t'.join(map(str, i)))
        
            
            



    

  