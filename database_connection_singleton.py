from configuration import load_config
import pyodbc


class DatabaseConnectionSingleton:
    conn = None

    @staticmethod
    def get_instance():
        if DatabaseConnectionSingleton.conn is None:
            config = load_config()

            server = config['server']
            database = config['database']
            username = config['username']
            password = config['password']

            DatabaseConnectionSingleton.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
                                                              + ';DATABASE=' + database + ';UID=' + username + ';PWD='
                                                              + password)

        return DatabaseConnectionSingleton.conn

    @staticmethod
    def begin_transaction():
        conn = DatabaseConnectionSingleton.get_instance()
        cursor = conn.cursor()
        cursor.execute('begin transaction;')

    @staticmethod
    def commit_transaction():
        conn = DatabaseConnectionSingleton.get_instance()
        cursor = conn.cursor()
        cursor.execute('commit transaction;')
        conn.commit()

    @staticmethod
    def close_connection():
        DatabaseConnectionSingleton.get_instance().close()
