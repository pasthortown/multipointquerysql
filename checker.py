from multipointquery import MultiPointQuery
from csv_writer import CSVWriter
import os
import shutil

csv_writer = CSVWriter()

def get_data(servers_list, query_to_exec):
    mpq = MultiPointQuery(servers_list, query_to_exec)
    server_data = mpq.exec_query()
    return server_data

def group_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)

toCompareFrom = [
    {
        "server": 'server',
        "database": 'bdd',
        "username": 'user',
        "password": 'pass',
        "port": '1433'
    }
]

servers = [
    {
        "server": 'server',
        "database": 'bdd',
        "username": 'user',
        "password": 'pass',
        "port": '1433'
    },
    {
        "server": 'server',
        "database": 'bdd',
        "username": 'user',
        "password": 'pass',
        "port": '1433'
    }
]

groups = [
    'Botones',
    'Cadena',
    'Estacion',
    'Formapago',
    'Menu',
    'Plus',
    'Restaurante',
    'Usuarios',
    'Promociones',
    'Pais'
]


for group in groups:
    group_folder(group)
    if (group == 'Pais'):
        query = '''SELECT GROUPNAMEColeccionDeDatos.IDColeccionGROUPNAME, GROUPNAMEColeccionDeDatos.IDColeccionDeDatosGROUPNAME FROM ColeccionGROUPNAME 
            INNER JOIN ColeccionDeDatosGROUPNAME ON ColeccionGROUPNAME.IDColeccionGROUPNAME = ColeccionDeDatosGROUPNAME.IDColeccionGROUPNAME 
            INNER JOIN GROUPNAMEColeccionDeDatos ON ColeccionGROUPNAME.IDColeccionGROUPNAME = GROUPNAMEColeccionDeDatos.IDColeccionGROUPNAME AND ColeccionDeDatosGROUPNAME.IDColeccionDeDatosGROUPNAME = GROUPNAMEColeccionDeDatos.IDColeccionDeDatosGROUPNAME;''' 
    else:
        query = '''SELECT GROUPNAMEColeccionDeDatos.ID_ColeccionGROUPNAME, GROUPNAMEColeccionDeDatos.ID_ColeccionDeDatosGROUPNAME FROM ColeccionGROUPNAME 
                INNER JOIN ColeccionDeDatosGROUPNAME ON ColeccionGROUPNAME.ID_ColeccionGROUPNAME = ColeccionDeDatosGROUPNAME.ID_ColeccionGROUPNAME 
                INNER JOIN GROUPNAMEColeccionDeDatos ON ColeccionGROUPNAME.ID_ColeccionGROUPNAME = GROUPNAMEColeccionDeDatos.ID_ColeccionGROUPNAME AND ColeccionDeDatosGROUPNAME.ID_ColeccionDeDatosGROUPNAME = GROUPNAMEColeccionDeDatos.ID_ColeccionDeDatosGROUPNAME;'''
    query = query.replace("GROUPNAME", group)
    if (group == 'Promociones'):
        query = '''SELECT PromocionesColeccionDeDatos.IDColeccionPromociones, PromocionesColeccionDeDatos.IDColeccionDeDatosPromociones FROM ColeccionPromociones 
            INNER JOIN ColeccionDeDatosPromociones ON ColeccionPromociones.ID_ColeccionPromociones = ColeccionDeDatosPromociones.ID_ColeccionPromociones 
            INNER JOIN PromocionesColeccionDeDatos ON ColeccionPromociones.ID_ColeccionPromociones = PromocionesColeccionDeDatos.IDColeccionPromociones AND ColeccionDeDatosPromociones.ID_ColeccionDeDatosPromociones = PromocionesColeccionDeDatos.IDColeccionDeDatosPromociones;'''
    azure_data = get_data(toCompareFrom, query)[0]["data"]
    if len(azure_data) > 0:
        csv_writer.write_json_to_csv(group + '\\azure.csv', azure_data)
        to_compare_data = get_data(servers, query)
