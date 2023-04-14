from database_connection_singleton import DatabaseConnectionSingleton


def insert_kinosal(oznaceni: str, kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'insert into kinosal (oznaceni, kapacita) values (\'{oznaceni}\', {kapacita});'
        .format(oznaceni=oznaceni, kapacita=kapacita))


def select_all_kinosal():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from kinosal;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_kinosal_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from kinosal where id = {id};'.format(id=id))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_kinosal_by_oznaceni(oznaceni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from kinosal where oznaceni = \'{oznaceni}\';'.format(oznaceni=oznaceni))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_kinosal_by_kapacita(kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from kinosal where kapacita = {kapacita};'.format(kapacita=kapacita))
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def update_kinosal_by_id(id: int, oznaceni: str, kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('update kinosal set oznaceni = \'{oznaceni}\', kapacita = {kapacita} where id = {id};'
                   .format(oznaceni=oznaceni, kapacita=kapacita, id=id))


def update_kinosal_by_oznaceni(ooznaceni: str, oznaceni: str, kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'update kinosal set oznaceni = \'{oznaceni}\', kapacita = {kapacita} where oznaceni = \'{ooznaceni}\';'
        .format(oznaceni=oznaceni, kapacita=kapacita, ooznaceni=ooznaceni))


def update_kinosal_by_kapacita(okapacita: int, oznaceni: str, kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'update kinosal set oznaceni = \'{oznaceni}\', kapacita = {kapacita} where kapacita = {okapacita};'
        .format(oznaceni=oznaceni, kapacita=kapacita, okapacita=okapacita))


def update_all_kinosal(oznaceni: str, kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute(
        'update kinosal set oznaceni = \'{oznaceni}\', kapacita = {kapacita};'
        .format(oznaceni=oznaceni, kapacita=kapacita))


def delete_kinosal_by_id(id: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kinosal where id = {id};'.format(id=id))


def delete_kinosal_by_oznaceni(oznaceni: str):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kinosal where oznaceni = \'{oznaceni}\';'.format(oznaceni=oznaceni))


def delete_kinosal_by_kapacita(kapacita: int):
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kinosal where kapacita = {kapacita};'.format(kapacita=kapacita))


def delete_all_kinosal():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('delete from kinosal;')


def select_kinosal_row_count():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select count(*) from kinosal;')
    rows = list()
    for row in cursor:
        rows.append(list(row))
    return rows[0][0]
