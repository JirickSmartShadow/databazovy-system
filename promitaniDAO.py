from database_connection_singleton import DatabaseConnectionSingleton
from datetime import datetime


def insert_promitani(film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('insert into promitani (film_id, kinosal_id, datum_cas) '
                   'values ({film_id}, {kinosal_id}, \'{datum_cas}\');'
                   .format(film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def select_promitani_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from promitani where id = {id};'.format(id=id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_promitani_by_film_id(film_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from promitani where film_id = {film_id};'.format(film_id=film_id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_promitani_by_kinosal_id(kinosal_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from promitani where kinosal_id = {kinosal_id};'.format(kinosal_id=kinosal_id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_promitani_by_datum_cas(datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from promitani where datum_cas = \'{datum_cas}\';'.format(datum_cas=datum_cas))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_all_promitani():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from promitani;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def update_promitani_by_id(id: int, film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update promitani set film_id = {film_id}, kinosal_id = {kinosal_id}, '
                   'datum_cas = \'{datum_cas}\' where id = {id};'
                   .format(id=id, film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def update_promitani_by_film_id(ofilm_id: int, film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update promitani set film_id = {film_id}, kinosal_id = {kinosal_id}, '
                   'datum_cas = \'{datum_cas}\' where film_id = {ofilm_id};'
                   .format(ofilm_id=ofilm_id, film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def update_promitani_by_kinosal_id(okinosal_id: int, film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update promitani set film_id = {film_id}, kinosal_id = {kinosal_id}, '
                   'datum_cas = \'{datum_cas}\' where kinosal_id = {okinosal_id};'
                   .format(okinosal_id=okinosal_id, film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def update_promitani_by_datum_cas(odatum_cas: datetime, film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update promitani set film_id = {film_id}, kinosal_id = {kinosal_id}, '
                   'datum_cas = \'{datum_cas}\' where datum_cas = \'{odatum_cas}\';'
                   .format(odatum_cas=odatum_cas, film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def update_all_promitani(film_id: int, kinosal_id: int, datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update promitani set film_id = {film_id}, kinosal_id = {kinosal_id}, '
                   'datum_cas = \'{datum_cas}\';'
                   .format(film_id=film_id, kinosal_id=kinosal_id, datum_cas=datum_cas))


def delete_promitani_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from promitani where id = {id};'.format(id=id))


def delete_promitani_by_film_id(film_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from promitani where film_id = {film_id};'.format(film_id=film_id))


def delete_promitani_by_kinosal_id(kinosal_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from promitani where kinosal_id = {kinosal_id};'.format(kinosal_id=kinosal_id))


def delete_promitani_by_datum_cas(datum_cas: datetime):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from promitani where datum_cas = \'{datum_cas}\';'.format(datum_cas=datum_cas))


def delete_all_promitani():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from promitani;')


def select_promitani_row_count():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select count(*) from promitani;')
    rows = list()
    for row in cursor:
        rows.append(list(row))
    return rows[0][0]
