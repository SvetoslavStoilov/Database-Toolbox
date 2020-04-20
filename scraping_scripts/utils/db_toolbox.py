import mysql.connector
from mysql.connector import Error
from config import config_dict
import sys


class db_toolbox:
    def __init__(self, user, password, host, database, autocommit):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.autocommit = autocommit
        self.connection = None
        self.cursor = None
        self.connect()

    def __del__(self):
        self.connection.close()
        print("Connection has been closed.")

    def connect(self):
        self.connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            database=self.database,
        )
        if self.connection.is_connected():
            print("Connected to MySQL database...")
        self.cursor = self.connection.cursor()

        self.connection.autocommit = self.autocommit

    def write_query(self, query):
        self.cursor.execute(query)
        print("{} executed successfuly".format(query))

    def read_query(self, query):
        self.cursor.execute(query)
        fetched = self.cursor.fetchall()
        print("{} executed successfuly".format(query))
        return fetched

    def multiple_insert(self, table, columns, values):

        #### table = table name --> 'table_name'
        #### columns = list of columns --> columns = ['col1','col2','coln']
        #### values = list of tuples --> values = [('some_heading','some_description', etc), ('some_heading2', ... etc.)]

        if not isinstance(values[0], tuple) and isinstance(values, list):
            print("The input of multiple insert is not list of tuples.")
            sys.exit()

        if isinstance(columns, list) or isinstance(columns, tuple):
            columns_string = ", ".join(columns)

        values_string = ", ".join(["%s" for col in range(len(values[0]))])
        operation = (
            f"INSERT IGNORE INTO {table} ({columns_string}) VALUES ({values_string})"
        )
        self.cursor.executemany(operation, values)


def db_con(config):
    con = db_toolbox(**config)
    return con
