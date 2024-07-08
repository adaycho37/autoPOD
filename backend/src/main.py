from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from supabase import create_client, Client
from json import loads, dumps

import pandas as pd
import os

from modules.dataframeManager import dataframeManager
from modules.functions import pandasJsonFormatter

# Variables de entorno
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Supabase
supabase: Client = create_client(url, key)

# FastAPI
app = FastAPI()

# Carga de Pandas
data = {}
master = dataframeManager()

# Petición que devolverá la tabla master en formato JSON
@app.get("/master")
async def read_root():
    result = master.getMaster().to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)
    return parsed

# Petición que devolverá los pdi del curso deseado en formato JSON
@app.get("/pdi/{curso}")
async def read_root(curso):
    curso = master.getYear(curso)
    tabla = curso.getTable("pdi")
    return pandasJsonFormatter(tabla)

# Petición que devolverá las asignaturas del curso deseado en formato JSON
@app.get("/asignatura/{curso}")
async def read_root(curso):
    curso = master.getYear(curso)
    tabla = curso.getTable("asignatura")
    return pandasJsonFormatter(tabla)

# Petición que devolverá el encargo docente del curso deseado en formato JSON
@app.get("/encargoDocente/{curso}")
async def read_root(curso):
    curso = master.getYear(curso)
    tabla = curso.getTable("encargoDocente")
    return pandasJsonFormatter(tabla)

# Petición que devolverá el pdi del curso deseado en formato JSON
@app.get("/pdi/{curso}/{id_PDI}")
async def read_root(curso, id_PDI:int):
    curso = master.getYear(curso)
    tabla = curso.getTable("pdi")
    pdi =  tabla[tabla['ID_PDI'] == id_PDI]
    result = pdi.to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)[0]

    # Atributo de ejemplo calculado
    encargo = curso.getTable("encargoDocente")[curso.getTable("encargoDocente")['ID_PDI'] == id_PDI]
    asignacion_total = 0
    for i in range(len(encargo)):
        row = encargo.iloc[i]
        for j in ['T', 'PA', 'PE/PX', 'TU']:
            if row['Creditos ' + j] != 0:
                asignacion_total += row['Creditos ' + j]*len(row['Grupos ' + j].split(","))
    parsed["Asignación_Total"] =  str(asignacion_total)
    return parsed


# Petición que devolverá la asignatura del curso deseado en formato JSON
@app.get("/asignatura/{curso}/{id_asignatura}")
async def read_root(curso, id_asignatura:int):
    curso = master.getYear(curso)
    tabla = curso.getTable("asignatura")
    asignatura =  tabla[tabla['ID_Asignatura'] == id_asignatura]
    result = asignatura.to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)[0]
    return parsed

# Petición que devolverá el encargo docente en el curso deseado de la asignatura deseada en formato JSON
@app.get("/encargoDocente/{curso}/pdi/{id_PDI}")
async def read_root(curso, id_PDI:int):
    curso = master.getYear(curso)
    tabla = curso.getTable("encargoDocente")
    encargoDocente =  tabla[tabla['ID_PDI'] == id_PDI]
    result = encargoDocente.to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)
    return parsed

# Petición que devolverá el encargo docente en el curso deseado del PDI deseado en formato JSON
@app.get("/encargoDocente/{curso}/asignatura/{id_asignatura}")
async def read_root(curso, id_asignatura:int):
    curso = master.getYear(curso)
    tabla = curso.getTable("encargoDocente")
    encargoDocente =  tabla[tabla['ID_Asignatura'] == id_asignatura]
    result = encargoDocente.to_json(orient='records', indent=4, force_ascii=False)
    parsed = loads(result)
    return parsed

# Petición que realiza un guardado
@app.get("/save")
async def read_root():
    master.save()
    return "Ok"