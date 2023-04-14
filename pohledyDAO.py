from database_connection_singleton import DatabaseConnectionSingleton


def select_all_prehled_filmu():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from prehled_filmu;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_all_prehled_promitani():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from prehled_promitani;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows


def select_all_celkovy_promitaci_cas():
    conn = DatabaseConnectionSingleton.get_instance()
    cursor = conn.cursor()
    cursor.execute('select * from celkovy_promitaci_cas;')
    rows = list()
    rows.append([i[0] for i in cursor.description])
    for row in cursor:
        rows.append(list(row))
    return rows
