from datetime import date
from database_connection_singleton import DatabaseConnectionSingleton


def insert_reziser(jmeno: str, prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('insert into reziser (jmeno, prijmeni) values '
                   '(\'{jmeno}\', \'{prijmeni}\');'
                   .format(jmeno=jmeno, prijmeni=prijmeni))


def select_all_reziser():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from reziser;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_reziser_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from reziser where id = {id};'.format(id=id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_reziser_by_jmeno(jmeno: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from reziser where jmeno = \'{jmeno}\';'.format(jmeno=jmeno))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_reziser_by_prijmeni(prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from reziser where prijmeni = \'{prijmeni}\';'.format(prijmeni=prijmeni))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def update_reziser_by_id(id: int, jmeno: str, prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update reziser set jmeno = \'{jmeno}\', prijmeni = \'{prijmeni}\', '
                   'where id = {id};'
                   .format(jmeno=jmeno, prijmeni=prijmeni, id=id))


def update_reziser_by_jmeno(ojmeno: str, jmeno: str, prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update reziser set jmeno = \'{jmeno}\', prijmeni = \'{prijmeni}\', '
                   'where jmeno = \'{ojmeno}\';'
                   .format(jmeno=jmeno, prijmeni=prijmeni, ojmeno=ojmeno))


def update_reziser_by_prijmeni(oprijmeni: str, jmeno: str, prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update reziser set jmeno = \'{jmeno}\', prijmeni = \'{prijmeni}\', '
                   'where prijmeni = \'{oprijmeni}\';'
                   .format(jmeno=jmeno, prijmeni=prijmeni, oprijmeni=oprijmeni))


def update_all_reziser(jmeno: str, prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update reziser set jmeno = \'{jmeno}\', prijmeni = \'{prijmeni}\';'
                   .format(jmeno=jmeno, prijmeni=prijmeni))


def delete_reziser_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from reziser where id = {id};'.format(id=id))


def delete_reziser_by_jmeno(jmeno: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from reziser where jmeno = \'{jmeno}\';'.format(jmeno=jmeno))


def delete_reziser_by_prijmeni(prijmeni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from reziser where prijmeni = \'{prijmeni}\';'.format(prijmeni=prijmeni))


def delete_all_reziser():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from reziser;')


def select_reziser_row_count():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select count(*) from reziser;')
    rows = list()
    for row in cursor:
        rows.append(list(row))
    return rows[0][0]
