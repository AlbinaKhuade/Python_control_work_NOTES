from logger import logging
import model as m
import check_in
from prettytable import PrettyTable

def menu():
    print()
    print('Добро пожаловать в приложение "ЗАМЕТКИ"!')
    logging.info('Start program')
    while True:
        type_num = input('\n*****Главное меню*****\nВыберите пункт меню:\n'
                         '1 - Показать все записи\n'
                         '2 - Найти запись\n'
                         '3 - Добавить запись\n'
                         '4 - Редактировать запись\n'
                         '5 - Удалить запись\n'
                         '0 - Выход\n')
        type_num = check_in.check_type_num(type_num)

        if type_num not in range(6):
            logging.error('Error: wrong main menu selection')
            print("Такого пункта меню нет.")
            continue

        elif type_num == 1:  # показать все записи
            print('Все заметки:')
            m.get_table('Notes.csv')
            print('Вы будете перемещены в главное меню.')

        elif type_num == 2:  # найти запись
            d = (input('Введите данные для поиска: '))
            m.find_info('Notes.csv', d)
            print('Вы будете перемещены в главное меню.')

        elif type_num == 3:  # добавить запись
            print('Добавление новой заметки...')
            m.add_text('Notes.csv')
            print('Вы будете перемещены в главное меню.')

        elif type_num == 4:  # редактировать запись
            note_id = input('Введите id заметки, данные которой Вы хотите изменить:\n')
            note_id = check_in.check_type_num(note_id)
            if note_id == -1:
                logging.error('Error: incorrect id entered.')
                print('Введенный id не существует. Проверьте корректность ввода.')
            else:  
                r_note_id = check_in.check_id_exist('Notes.csv', note_id)
                if r_note_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('Введенный id не существует. Проверьте корректность ввода.')
                else:
                    num = input('\nКакие изменения вы хотите внести:\n' 
                                '1 - Изменить название заметки\n'
                                '2 - Изменить текст заметки\n'
                                '3 - Изменить имя автора заметки\n'
                                '4 - Изменить все данные\n')
                    num = check_in.check_type_num(num)
                    if num in range(1, 5):
                        m.change_info('Notes.csv', note_id, num)
                        print('Вы будете перемещены в главное меню.')
                    else:
                        logging.error('Error: wrong submenu selection')
                        print("Такого пункта меню нет. Повторите выбор меню.")
                        continue
            

        elif type_num == 5:  # удалить запись
            note_id = input('Введите id заметки, которую Вы хотите удалить:\n')
            note_id = check_in.check_type_num(note_id)
           
            if note_id == -1:
                logging.error('Error: incorrect id entered.')
                print('Введенный id не существует. Проверьте корректность ввода.')
            else:   
                r_note_id = check_in.check_id_exist('Notes.csv', note_id)
                if r_note_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('Введенный id не существует. Проверьте корректность ввода.')
                else:
                    m.delete_info('Notes.csv', r_note_id)
            print('Вы будете перемещены в главное меню.')

        elif type_num == 0:  # выход
            logging.info("Stop program")
            print('Спасибо, что воспользовались нашей программой!\n')
            break

