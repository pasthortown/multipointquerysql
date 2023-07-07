from connect import SQLServerConnection

class MultiPointQuery:
    def __init__(self, servers, query):
        self.servers = servers
        self.query = query

    def exec_query(self):
        servers_data = []
        for server in self.servers:
            sql_connection = SQLServerConnection(server["server"], server["database"], server["username"], server["password"], server["port"])
            sql_connection.connect()
            result = sql_connection.execute_query(self.query)
            sql_connection.close()
            servers_data.append({"server": server, "data":result})
        return servers_data
    
