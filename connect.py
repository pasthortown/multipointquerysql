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
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            row_array = []
            for value in row:
                row_array.append(str(value))
            results.append(dict(zip(columns, row_array)))
        result_json = results
        cursor.close()
        return result_json

    def close(self):
        if self.connection:
            self.connection.close()
