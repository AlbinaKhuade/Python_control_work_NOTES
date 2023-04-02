from os import path
import csv 
from logger import logging
from prettytable import PrettyTable
import sys
from datetime import datetime

def last_id():
    with open('last_id.txt', 'r', encoding='utf-8') as l_f:
        last_id = l_f.read()
        return last_id
# дозапись  
def write_file(file, data):
        with open(file, 'a', encoding='utf-8') as t_file:  
            file_writer = csv.writer(t_file, delimiter = ";", lineterminator="\r")
            file_writer.writerow(data)


# перезапись 
def write_file_w(file, data):
    with open(file, 'w', encoding='utf-8') as t_file:  
        file_writer = csv.writer(t_file, delimiter = ";", lineterminator="\r")
        file_writer.writerow(data)
 
# чтение
def read_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as t_file:
            csv.reader(t_file, delimiter=';')   
            all_notes = []
            for row in t_file:   
                str_note = "".join(row)
                list_notes = str_note.strip().split(';')
                all_notes.append(list_notes)       
        return all_notes
    else:
        print("The files do not exist in the system!")

# метод вывода таблицы со всеми заметками
def get_table(file): 
    list_all_notes=read_file(file) 
    t = PrettyTable(list_all_notes[0])
    for i in range(1, len(list_all_notes)):
        t.add_row(list_all_notes[i])
    print(t)

# поиск
def find_info(file, data):
    find_list = []
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        for j in range(len(list_all_notes[i])):
            if list_all_notes[i][j] == data:
                find_list.append(list_all_notes[i])
            else: pass
    for k in range(len(find_list)+1):
        if k == 0:
            write_file_w('Find_info.csv', list_all_notes[k])
        else:
            write_file('Find_info.csv', find_list[k-1])  
    if len(find_list) == 0:
        print('По Вашему запросу не найдена ни одна заметка')
    else:
        print('Информация по вашему запросу:')                
        get_table('Find_info.csv')


# дозапись
def add_text(file):
    id = last_id()
    id = int(id) + 1
    id_w = str(id)
    with open('last_id.txt','w', encoding='utf-8') as l_f:
        l_f.write(id_w)
    header = input('Введите заголовок заметки: ')
    note_content = input('Введите текст заметки: ')
    author = input('Введите имя автора заметки: ')
    note_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    new_note = [id, header, note_content, author, note_date]
    write_file(file, new_note)
    print('Заметка успешно добавлена!')
    print('Обновлённый список заметок:')
    get_table('Notes.csv')

# замена
def change_info(file, n_id, op):
    list_all_notes = read_file(file)
    for i in range(1,len(list_all_notes)):
        if list_all_notes[i][0] == str(n_id):
            if op == 1:
                list_all_notes[i][1] = input('Введите новый заголовок заметки: ')
                note_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                list_all_notes[i][4] = note_date
            elif op == 2:
                list_all_notes[i][2] = input('Введите новый текст заметки: ')
                note_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                list_all_notes[i][4] = note_date
            elif op == 3:
                list_all_notes[i][3] = input('Введите новое имя автора заметки: ')
                note_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                list_all_notes[i][4] = note_date
            elif op == 4:
                list_all_notes[i][1] = input('Введите новый заголовок заметки: ')
                list_all_notes[i][2] = input('Введите новый текст заметки: ')
                list_all_notes[i][3] = input('Введите новое имя автора заметки: ')
                note_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                list_all_notes[i][4] = note_date
    for j in range(len(list_all_notes)):
        if j == 0:
            write_file_w(file, list_all_notes[j])
        else:
            write_file(file, list_all_notes[j])
    print('Данные успешно изменены!')
    print('Обновлённый список заметок:')
    get_table('Notes.csv') 


# удаление
def delete_info(file, n_id):
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        if list_all_notes[i][0] == str(n_id):
            list_all_notes.pop(i)
            break
    for j in range(len(list_all_notes)):
        if j == 0:
            write_file_w(file, list_all_notes[j])
        else:
            write_file(file, list_all_notes[j])
    print('Заметка успешно удалена!')        
    print('Обновлённый список заметок:')        
    get_table('Notes.csv')
