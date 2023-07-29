from model import *
from view import *
from db import *


def menu (db_note: dict, last_id) -> None:
    while True:
        status = print_menu()
        if status == '1':
            tittle = get_data("Введите заголовок: ")
            body = get_data("Введите заметку: ")
            db_note, last_id = create_note(db_note, last_id, tittle, body)
        if status == '2':
            print_db_note(db_note)   
        if status == '3':
            filepath = get_data("Введите имя файла: ")
            # delimeter = get_data("Введите разделитель: ")
            export_db_note(db_note, filepath)
            print_message(f"Данные сохранены в файл {filepath}")

        if status == '4':
            filepath = get_data("Введите имя файла: ")
            # delimeter = get_data("Введите разделитель: ")
            db_note,last_id = import_db_note(db_note, filepath, last_id)


        if status == '5':
            menu_filt(db_note)
        if status == '6':
            print_short_db_note(db_note)
            id = int(get_data("Введите id заметки, чтобы ее удалить: "))
            delete_note(db_note, id)
            print_message("Заметка удалена.")
        if status == '7':
            print_short_db_note(db_note)
            id = int(get_data("Введите id заметки, чтобы ее изменить: "))
            ch_note_tittle = get_data("Введите новый заголовок заметки, если не хотите менять заголовок нажмите Enter: ")
            ch_note_body = get_data("Введите новое тело заметки, если не хотите менять тело заметки нажмите Enter: ")
            change_note(db_note, id, ch_note_tittle, ch_note_body)
            print_message("Измененная заметка: ")
            print_note(db_note[id])
        elif status == '8':
            break



def menu_filt (db_note: dict) -> None:
        status = print_filt_menu()
        flag = False
        if status == '1':
            ID = int(get_data("Введите id заметки, чтобы ее найти: "))
            db_note, flag = find_note_by_filt_ID(db_note, ID)
            if flag:
                print_note(db_note)
            else: print_message(f"ID - {ID} не найден")

        if status == '2':
            filt_tittle = get_data("Введите заголовок или часть заголовка заметки, чтобы ее найти: ")
            intermediate_db_note, flag = find_note_by_filt_tittle(db_note, filt_tittle)
            if flag:
                print_db_note(intermediate_db_note)
            else: print_message(f"{filt_tittle} среди заголовков не найден")
        if status == '3':
            filt_body = get_data("Введите ключевое слово заметки (тело заметки), чтобы ее найти: ")
            intermediate_db_note, flag = find_note_by_filt_word(db_note, filt_body)
            if flag:
                print_db_note(intermediate_db_note)
            else: print_message(f"{filt_body} среди заметок не найден")

        if status == '4':
            year, month, day = get_date()
            filt_date_start_str = collect_date(year, month, day)
            year, month, day = get_date()
            filt_date_end_str = collect_date(year, month, day)
            intermediate_db_note, flag = find_note_by_filt_date(db_note, filt_date_start_str, filt_date_end_str)
            if flag:
                print_db_note(intermediate_db_note)
            else: print_message("В указанном диапазоне заметки не найдены")            

def get_date ():
    year = ""
    month = ""
    day = ""

    flag = False
    print_message("Введите дату.")
    while not flag:
        year = get_data("Введите год: ")
        if not year.isdigit() :
            print_message("Некорректный формат года.")
        else:
            flag = True

    flag = False 
    while not flag:
        month = get_data("Введите номер месяца: ")
        if not month.isdigit(): 
            print_message("Некорректный формат месяца.")
        elif int(month) < 0 or int(month) > 12:
            print_message("Некорректный формат месяца.")
        else:
            flag = True

    flag = False 
    while not flag:
        day = get_data("Введите день месяца: ")
        if not day.isdigit() : print_message("Некорректный формат дня.")
        elif day.isdigit():
            if int(day) < 0 or int(day) > 31:
                print_message("Некорректный формат дня.")
            else:     
                match month:
                    case 4,6,9,11:
                        if int(day) > 30:
                            print_message("Некорректный формат дня.")
                        else: flag = True

                    case 2:
                        if int(year) // 400 == 0:
                            if int(day) > 29:
                                print_message("Некорректный формат дня.")
                            else: flag = True
                        elif int(year) // 4 == 0 and int(year) // 100 != 0:
                            if int(day) > 29:
                                print_message("Некорректный формат дня.")
                            else: flag = True
                        else:
                            if int(day) > 28:
                                print_message("Некорректный формат дня.")
                            else: flag = True

                flag = True
    return year, month, day




