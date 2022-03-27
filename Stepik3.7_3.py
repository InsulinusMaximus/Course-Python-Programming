#1
d_num = int(input())
d = []
for _ in range (d_num):
    d.append(str(input().lower()))
print(d)
l_num = int(input())
l = []
for _ in range (l_num):
    l.append(input().split(" "))

mistekes = []

for string in l:
    for word in string:
        word_low = word.lower()
        if word_low not in d:
            if word_low not in mistekes:
                mistekes.append(word_low)
                print(word_low)
