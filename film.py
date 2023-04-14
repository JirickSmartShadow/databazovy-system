from filmDAO import *
from lib.data_formatting import *


def get_all_film():
    rows = select_all_film()
    output = format_data(rows)
    return output


def add_film(kategorie_id: int, reziser_id: int, nazev: str, delka_min: int, cena: float, tri_d: bool):
    insert_film(kategorie_id, reziser_id, nazev, delka_min, cena, tri_d)


def change_film(id: int, kategorie_id: int, reziser_id: int, nazev: str, delka_min: int, cena: float, tri_d: bool):
    update_film_by_id(id, kategorie_id, reziser_id, nazev, delka_min, cena, tri_d)


def remove_film(id: int):
    delete_film_by_id(id)


def get_film_row_count():
    row_count = select_film_row_count()
    return row_count
