from reziserDAO import *
from lib.data_formatting import *


def get_all_reziser():
    rows = select_all_reziser()
    output = format_data(rows)
    return output


def add_reziser(jmeno: str, prijmeni: str):
    insert_reziser(jmeno, prijmeni)


def change_reziser(id: int, jmeno: str, prijmeni: str):
    update_reziser_by_id(id, jmeno, prijmeni)


def get_reziser_row_count():
    row_count = select_reziser_row_count()
    return row_count
