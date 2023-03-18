import pandas as pd
from sodapy import Socrata

client = Socrata("www.datos.gov.co", None )
# results = client.get ("ch4u-f3i5", limit =2000)


def consultaEspecifica(limite, departamento, municipio, cultivo, columnas):
    # Consulta los datos para el departamento, municipio y cultivo especificados
    results = client.get("ch4u-f3i5", 
                         limit=limite, 
                         where=f"departamento = '{departamento}' AND municipio = '{municipio}' AND cultivo = '{cultivo}'", 
                         select=",".join(columnas))

    # Encapsula los datos en un DataFrame de Pandas
    results_df = pd.DataFrame.from_records(results)
    results_df = results_df.rename(columns={'departamento': 'DEPARTAMENTO ', 'municipio': 'MUNICIPIO', 'cultivo': 'CULTIVO' })
    
    return results_df


    

