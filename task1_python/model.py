import datetime


def create_note(db_note: dict, id: int, tittle: str, body: str):
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db_note[id] = {'id':id, 'tittle': tittle, 'body': body, 'date': date}
    id += 1
    return db_note, id

def export_note_by_filt(id: str, tittle: str, body: str, date: str):
    note = {'id':id, 'tittle': tittle, 'body': body, 'date': date}
    return note


def delete_note(db_note: dict, delete_id) -> dict:
    if delete_id in db_note.keys():
        del db_note[delete_id]
        return db_note, True
    else: 
        return db_note, False


def find_note_by_filt_ID(db_note: dict, filt_id: int) -> dict:
    if int(filt_id) in db_note.keys():
        return db_note[int(filt_id)], True
    else:    
        return db_note, False

def find_note_by_filt_tittle(db_note: dict, filt_tittle: str) -> dict:
    intermediate_db_note = {}
    flag = False
    for idx, note in db_note.items():
        if filt_tittle.lower() in note['tittle'].lower():
            intermediate_db_note[idx] = export_note_by_filt(note['id'], note['tittle'], note['body'], note['date']) 
            flag = True 
    return intermediate_db_note, flag
             
def find_note_by_filt_word(db_note: dict, filt_body: str) -> dict:
    intermediate_db_note = {}
    flag = False
    for idx, note in db_note.items():
        if filt_body.lower() in note['body'].lower():
            intermediate_db_note[idx] = export_note_by_filt(note['id'], note['tittle'], note['body'], note['date'])
            flag = True 
    return intermediate_db_note, flag


def find_note_by_filt_date(db_note: dict, filt_date_start_str: str, filt_date_end_str: str) -> dict:
    intermediate_db_note = {}
    flag = False
   
    if filt_date_start_str == "":
        filt_date_start_str = db_note[0]['date']
    if filt_date_end_str == "":
        filt_date_end_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    filt_date_start = change_date_type(filt_date_start_str)
    filt_date_end = change_date_type(filt_date_end_str)
    if filt_date_start > filt_date_end: 
        cur = filt_date_start
        filt_date_start = filt_date_end
        filt_date_end = cur

    for idx, note in db_note.items():
        if change_date_type(note['date']) > filt_date_start and change_date_type(note['date']) < filt_date_end:
            intermediate_db_note[idx] = export_note_by_filt(note['id'], note['tittle'], note['body'], note['date']) 
            flag = True 
    return intermediate_db_note, flag        


def change_date_type(date_str: str) -> datetime:
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    date.strftime("%Y-%m-%d %H:%M:%S")
    return date
    
def collect_date(year, month, day) -> str:
    hour = "00"
    minute = "00"
    second = "00" 
    return f"{year}-{day}-{month} {hour}:{minute}:{second}"

def change_note(db_note: dict, id: int, ch_note_tittle: str, ch_note_body: str) -> None:
    if len(ch_note_tittle) > 0: db_note[id]['tittle'] = ch_note_tittle
    if len(ch_note_body) > 0: db_note[id]['body'] = ch_note_body
    db_note[id]['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")




