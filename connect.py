import pyodbc

class SQLServerConnection:
    def __init__(self, server, database, username, password, port=1433):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.port = port
        self.connection = None

    def connect(self):
        connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server},{self.port};DATABASE={self.database};UID={self.username};PWD={self.password}"
        self.connection = pyodbc.connect(connection_string)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        if self.connection:
            self.connection.close()
