from database_connection_singleton import DatabaseConnectionSingleton


def insert_film(kategorie_id: int, reziser_id: int, nazev: str, delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'insert into film (kategorie_id, reziser_id, nazev, delka_min, cena, tri_d) '
        'values ({kategorie_id}, {reziser_id}, \'{nazev}\', {delka_min}, {cena}, {tri_d});'
        .format(kategorie_id=kategorie_id, reziser_id=reziser_id, nazev=nazev,
                delka_min=delka_min, cena=cena, tri_d=tri_d))


def select_film_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where id = {id};'.format(id=id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_kategorie_id(kategorie_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where kategorie_id = {kategorie_id};'.format(kategorie_id=kategorie_id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_reziser_id(reziser_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where reziser_id = {reziser_id};'.format(reziser_id=reziser_id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_nazev(nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where nazev = \'{nazev}\';'.format(nazev=nazev))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_delka_min(delka_min: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where delka_min = {delka_min};'.format(delka_min=delka_min))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_cena(cena: float):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where cena = {cena};'.format(cena=cena))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_film_by_tri_d(tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film where tri_d = {tri_d};'.format(tri_d=tri_d))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_all_film():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from film;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def update_film_by_id(id: int, kategorie_id: int, reziser_id: int, nazev: str,
                      delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where id = {id};'
                   .format(id=id, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_kategorie_id(okategorie_id: int, kategorie_id: int, reziser_id: int, nazev: str,
                                delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where kategorie_id = {okategorie_id};'
                   .format(okategorie_id=okategorie_id, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_reziser_id(oreziser_id: int, kategorie_id: int, reziser_id: int, nazev: str,
                              delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where reziser_id = {oreziser_id};'
                   .format(oreziser_id=oreziser_id, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_nazev(onazev: str, kategorie_id: int, reziser_id: int, nazev: str,
                         delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where nazev = \'{onazev}\';'
                   .format(onazev=onazev, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_delka_min(odelka_min: int, kategorie_id: int, reziser_id: int, nazev: str,
                             delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where delka_min = {odelka_min};'
                   .format(odelka_min=odelka_min, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_cena(ocena: int, kategorie_id: int, reziser_id: int, nazev: str,
                        delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where cena = {ocena};'
                   .format(ocena=ocena, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_film_by_tri_d(otri_d: int, kategorie_id: int, reziser_id: int, nazev: str,
                         delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0

    if otri_d is True:
        otri_d = 1
    else:
        otri_d = 0

    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, '
                   'tri_d = {tri_d} where tri_d = {otri_d};'
                   .format(otri_d=otri_d, kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def update_all_film(kategorie_id: int, reziser_id: int, nazev: str,
                    delka_min: int, cena: float, tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update film set kategorie_id = {kategorie_id}, reziser_id = {reziser_id}, '
                   'nazev = \'{nazev}\', delka_min = {delka_min}, cena = {cena}, tri_d = {tri_d};'
                   .format(kategorie_id=kategorie_id, reziser_id=reziser_id,
                           nazev=nazev, delka_min=delka_min, cena=cena, tri_d=tri_d))


def delete_film_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where id = {id};'.format(id=id))


def delete_film_by_kategorie_id(kategorie_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film kategorie_id  = {kategorie_id};'.format(kategorie_id=kategorie_id))


def delete_film_by_reziser_id(reziser_id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where reziser_id = {reziser_id};'.format(reziser_id=reziser_id))


def delete_film_by_nazev(nazev: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where nazev = \'{nazev}\';'.format(nazev=nazev))


def delete_film_by_delka_min(delka_min: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where delka_min = {delka_min};'.format(delka_min=delka_min))


def delete_film_by_cena(nazev: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where nazev = \'{nazev}\';'.format(nazev=nazev))


def delete_film_by_tri_d(tri_d: bool):
    if tri_d is True:
        tri_d = 1
    else:
        tri_d = 0
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film where tri_d = {tri_d};'.format(tri_d=tri_d))


def delete_all_film():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from film;')


def select_film_row_count():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select count(*) from film;')
    rows = list()
    for row in cursor:
        rows.append(list(row))
    return rows[0][0]
