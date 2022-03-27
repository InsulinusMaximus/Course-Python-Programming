# Программа считывает с файла строки, содержащие:
# <'Имя';'Оценка по математике';'Оценка по физике';'Оценка по русскому языку'>
# После выводит в файл строки со средней оценкой по каждому ученику
# А последней строкой выводятся средние оценки по каждому из предметов среи всех учеников

# Сохранениt файла в переменную
file_in = open('dataset_3363_4.txt', 'r')

# Инициализация двумерного списка
list = []

# Сохранение строк в двумерный список, где одна строка это отдельный список
for line in file_in.readlines():
    list.append([word for word in line.strip().split(';')])
#print(list)

# Функция, обрабатывающая двумерный массив, и возвращающая двумерный массив с значениями:
# <'Имя', 'Средняя оценка по всем предметам'> + последуу строку со средними значениями по каждому предмету среди всех учеников
def average(d):
    list = [[0 for _ in range(2)] for _ in range(len(d))]
    last_str = []
    count_stlb = count_str = 0
    matem = fisic = russ = 0
    for line in d:
        count_str = 0
        for mean in line:
            if count_str != 0:
                list[count_stlb][1] += int(mean)
                if count_str == 1:
                    matem += int(mean)
                elif count_str == 2:
                    fisic += int(mean)
                elif count_str == 3:
                    russ += int(mean)         
            else:
                list[count_stlb][0] = mean+':'
            count_str += 1
        else:
            list[count_stlb][1] = str(list[count_stlb][1]/3)+';'
        count_stlb += 1
    last_str.append('Subject average:')
    last_str.append(str(matem/count_stlb)+',')
    last_str.append(str(fisic/count_stlb)+',')
    last_str.append(str(russ/count_stlb)+'.')
    list.append(last_str)
    return list

# Вызов функции и дальнейший вывод полученных значений в файл
file_out = open('return3.4_3_1.txt', 'w')
for i in average(list):
    for j in i:
        j=str(j)
        file_out.write(j)
        file_out.write(' ')
    file_out.write('\n')
file_out.close()






