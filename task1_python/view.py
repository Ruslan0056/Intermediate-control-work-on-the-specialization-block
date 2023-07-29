def print_db_note(db_node: dict) -> None:
    for idx, note in db_node.items():    
        print(f"[{idx} | {note['tittle']} | {note['body']} | {note['date']}]")


def print_short_db_note(db_node: dict) -> None:
    for idx, note in db_node.items(): 
        print(f"[{idx} | {note['tittle']}]")
        
def print_note(note: dict) -> None:
    print(f"[{note['id']} | {note['tittle']} | {note['body']} | {note['date']}]")

def print_message(str: str) -> None:
    print(str) 

def get_data(str: str) -> str:
    return input(str) 

def print_menu() -> str:
    print('Возможные действие:')
    print('1 - Создать запись;')
    print('2 - Вывести данные;')
    print('3 - Экспортировать данные в файл;')
    print('4 - Импортировать данные из файла;')
    print('5 - Найти запись по фильтру;')
    print('6 - Удалить запись;')
    print('7 - Редактировать запись;')
    print('8 - Выход.')
    return input('Введите действие: ')

def print_filt_menu() -> str:
    print('Возможные действие:')
    print('1 - Фильтр по id;')
    print('2 - Фильтр по заголовку;')
    print('3 - Фильтр по ключевому слову (тело заметки);')
    print('4 - Фильтр по дате;')
    return input('Введите действие: ')

     

