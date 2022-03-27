'''
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


for i in range(len(list)):
        indstolb=i
        for j in range(len(list[i])):
            indstroki=j
            print(indstolb, indstroki)
'''
import openpyxl
print ('Hello')

