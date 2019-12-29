#!/usr/bin/env python3

import os
# нахожу путь до папки scripts, с помощью os.path.dirname из модуля os.path
# __file__ - равна пути до текущего файла.

path_to_scripts = os.path.dirname(__file__)

# нахожу путь до папки reports, где лежит отчет, как конкатенацию первого
# элемента кортежа результата функции os.path.split и строки с названием папки.

path_to_reports = os.path.split(path_to_scripts)[0] + '/reports/'

# файл отчета

file_name = 'report.txt'

# открываю файл отчета

current_report = open(path_to_reports + file_name)

# записываю заголовок в список, с помощью метода .split, который разделяет по разделителю
# '\t' - это табуляция.
head = (current_report.readline()).split('\t')
# создаю пустой список в который запишу весь файл
file_list = []
# создаю копию файла, по которой буду обегать в цикле for потому что поскольку append меняет по месту - появляются баги
copy = current_report
# считывают построчно данные из файла и записываю в file.list
for line in copy:
    file_list.append((current_report.readline()).split('\t'))
i = 0
# для проверки вывожу все на экран
print(head)
while i <= len(file_list)-1:
    print(file_list[i])
    i += 1

# закрываю файл
current_report.close()
def main():
    print()

if __name__ == '__main__':
    main()