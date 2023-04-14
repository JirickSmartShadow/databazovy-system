from kinosalDAO import *
from lib.data_formatting import *


def get_all_kinosal():
    rows = select_all_kinosal()
    output = format_data(rows)
    return output


def add_kinosal(oznaceni: str, kapacita: int):
    insert_kinosal(oznaceni, kapacita)


def change_kinosal(id: int, oznaceni: str, kapacita: int):
    update_kinosal_by_id(id, oznaceni, kapacita)


def remove_kinosal(id: int):
    delete_kinosal_by_id(id)


def get_kinosal_row_count():
    row_count = select_kinosal_row_count()
    return row_count
