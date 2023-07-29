def export_db_note(db_note: dict, filepath, delimeter: str = "#" ) -> None:
    with open(filepath, mode= 'w', encoding= 'utf-8' ) as file:
        for data in db_note.values():
            file.write(f"{data['id']}{delimeter}{data['tittle']}{delimeter}{data['body']}{delimeter}{data['date']}{delimeter}\n")


def import_db_note(db_note: dict, filepath: str, last_id: int, delimeter: str = "#" ) -> tuple:
    with open(filepath, mode= 'r', encoding= 'utf-8' ) as file:
        for line in file:
            _data = line.split(delimeter)
            db_note[last_id] = {'id': _data[0], 'tittle': _data[1], 'body': _data[2], 'date':_data[3]}
            last_id +=1
    return db_note, last_id

