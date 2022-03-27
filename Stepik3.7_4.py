#1
way_num = int(input())
ways = []
for _ in range (way_num):
    ways.append(input().split(' '))


x = y = 0
n = 'север'
w = 'запад'
s = 'юг'
e = 'восток'


for i in range(len(ways)):
    if ways[i][0] == n:
        way = int(ways[i][1])
        y += way
    elif ways[i][0] == w:
        way = int(ways[i][1])
        x -= way
    elif ways[i][0] == s:
        way = int(ways[i][1])
        y -= way
    elif ways[i][0] == e:
        way = int(ways[i][1])
        x += way
print(x, y)