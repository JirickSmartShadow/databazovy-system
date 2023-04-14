from database_connection_singleton import DatabaseConnectionSingleton


# def insert_kategorie(nazev: str):
#     conn = DatabaseConnectionSingleton.get_instance()
#     cursor = conn.cursor()
#     cursor.execute('insert into kategorie values (\'{nazev}\')'.format(nazev=nazev))


def select_all_kategorie():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select id, nazev from kategorie;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_kategorie_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select id, nazev from kategorie where id = {id};'.format(id=id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_kategorie_by_nazev(nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select id, nazev from kategorie where nazev = \'{nazev}\';'.format(nazev=nazev))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def update_kategorie_by_id(id: int, nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update kategorie set nazev = \'{nazev}\' where id = {id};'.format(nazev=nazev, id=id))


def update_kategorie_by_nazev(onazev: str, nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'update kategorie set nazev = \'{nazev}\' where nazev = \'{onazev}\';'.format(nazev=nazev, onazev=onazev))


def update_all_kategorie(nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'update kategorie set nazev = \'{nazev}\';'.format(nazev=nazev))


def delete_kategorie_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kategorie where id = {id};'.format(id=id))


def delete_kategorie_by_nazev(nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kategorie where nazev = \'{nazev}\';'.format(nazev=nazev))


def delete_all_kategorie():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kategorie;')


def select_kategorie_row_count():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select count(*) from kategorie;')
    rows = list()
    for row in cursor:
        rows.append(list(row))
    return rows[0][0]
