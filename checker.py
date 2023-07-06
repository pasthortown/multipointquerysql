from multipointquery import MultiPointQuery

servers = [
    {
        "server": 'IP_SERVER',
        "database": 'BDD',
        "username": 'usuario',
        "password": 'clave',
        "port": 'puerto'
    },
    {
        "server": 'IP_SERVER',
        "database": 'BDD',
        "username": 'usuario',
        "password": 'clave',
        "port": 'puerto'
    }
]

query = 'SELECT 1;'

mpq = MultiPointQuery(servers, query)

print(mpq.exec_query())
    
