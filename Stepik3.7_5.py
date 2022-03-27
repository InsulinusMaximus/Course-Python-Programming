#1


inf = open('dataset_3380_5.txt', 'r') 
array = [[word for word in line.strip().split()] for line in inf.readlines()]
#print(array)
new_array = []
for line in range(len(array)):
    for word in range(len(array[line])):
        if array[line][word].isdigit() == True:
            new_array.append(int(array[line][word]))

d = {}
for num in range(0,len(new_array),2):
    if new_array[num] not in d:
        d.update({new_array[num] : [new_array[num+1], 1]})
    else:
        d[new_array[num]][0] += new_array[num+1]
        d[new_array[num]][1] += 1

itog = {}

for i in d:
    value = d[i][0]/d[i][1]
    itog.update({i : value})
sort_itog = sorted(itog.items())
for i in sort_itog:
    print(*i)
