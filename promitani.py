from promitaniDAO import *
from lib.data_formatting import *


def get_all_promitani():
    rows = select_all_promitani()
    output = format_data(rows)
    return output


def add_promitani(film_id: int, kinosal_id: int, datum_cas: datetime):
    insert_promitani(film_id, kinosal_id, datum_cas)


def change_promitani(id: int, film_id: int, kinosal_id: int, datum_cas: datetime):
    update_promitani_by_id(id, film_id, kinosal_id, datum_cas)


def remove_promitani(id: int):
    delete_promitani_by_id(id)


def remove_promitani_by_film_id(film_id: int):
    delete_promitani_by_film_id(film_id)


def remove_promitani_by_kinosal_id(kinosal_id: int):
    delete_promitani_by_kinosal_id(kinosal_id)


def get_promitani_row_count():
    row_count = select_promitani_row_count()
    return row_count
