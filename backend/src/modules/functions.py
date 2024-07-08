import pandas as pd
from json import loads, dumps

# Función que exporta a json los dataframes de Pandas con el formato deseado
def pandasJsonFormatter(tabla):
    result = tabla.to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)
    return parsed