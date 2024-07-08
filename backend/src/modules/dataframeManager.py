import pandas as pd
from pathlib import Path

    
# Clase maestra que gestiona las distintos cursos que se emplean actualmente
class dataframeManager:

    # Constructor de la clase
    def __init__(self):
        try:
            self.__master = pd.read_csv("dataBase/master.csv")
        except:
            self.__master = pd.DataFrame(
            {
                "Curso": pd.Series(dtype='str'),
                "Estado": pd.Series(dtype='str'),
                "Modificable": pd.Series(dtype='str'),
                "Ultima_Modificacion": pd.Series(dtype='str'),
                "Ultimo_Calculo": pd.Series(dtype='str'),
            })
        self.__planificacion = yearDataframe(self.__master[self.__master['Estado'] == 'Planificación']['Curso'].iloc[0])
        self.__ejecucion = yearDataframe(self.__master[self.__master['Estado'] == 'Ejecución']['Curso'].iloc[0])

    # Método que realiza un guardado de las tablas
    def save(self):
        self.__master.to_csv('dataBase/master.csv', index=False)
        self.__planificacion.save()
        self.__ejecucion.save()

    # Getter de la tabla Master
    def getMaster(self):
        return self.__master
    
    # Método que devuelve el cruso deseado
    def getYear(self, curso):

        try:
            registro = self.__master[self.__master['Curso'] == curso]
            if registro['Estado'].iloc[0] == 'Planificación':
                return self.__planificacion
            elif registro['Estado'].iloc[0] == 'Ejecución':
                return self.__ejecucion
            else:
                return yearDataframe(registro['Curso'].iloc[0])
        
        except:
            return "Error"



# Clase que gestiona todos los dataframes de un mismo curso
class yearDataframe:

    # Constructor de la clase
    def __init__(self, curso):
        self.curso = curso

        try:
            self.__pdi = pd.read_csv("dataBase/" + curso + "/pdi.csv", sep=';')
            self.__asignatura = pd.read_csv("dataBase/" + curso + "/asignatura.csv", sep=';')
            self.__encargoDocente  = pd.read_csv("dataBase/" + curso + "/encargoDocente.csv", sep=';')
       
        except:
            Path("dataBase/" + curso).mkdir(parents=True, exist_ok=True)
            self.__pdi = pd.DataFrame(
            {
                "ID_PDI": pd.Series(dtype='str'),
                "Nombre": pd.Series(dtype='str'),
                "Area": pd.Series(dtype='str'),
                "Categoría": pd.Series(dtype='str'),
                "Exceso": pd.Series(dtype='str'),
            })
            
            self.__asignatura = pd.DataFrame(
            {
                "ID_Asignatura": pd.Series(dtype='str'),
                "Denominación": pd.Series(dtype='str'),
                "Master": pd.Series(dtype='str'),
                "Especial": pd.Series(dtype='str'),
                "Ofertada": pd.Series(dtype='str'),
                "Tipología": pd.Series(dtype='str'),
                "Plan": pd.Series(dtype='str'),
                "Tipología": pd.Series(dtype='str'),
                "Curso": pd.Series(dtype='str'),
                "Cuatrimestre": pd.Series(dtype='str'),
                "Docencia_Area": pd.Series(dtype='str'),
                "Creditos T1": pd.Series(dtype='str'),
                "Grupos T1": pd.Series(dtype='str'),
                "Creditos T2": pd.Series(dtype='str'),
                "Grupos T2": pd.Series(dtype='str'),
                "Creditos T3": pd.Series(dtype='str'),
                "Grupos T3": pd.Series(dtype='str'),
                "Creditos T3a": pd.Series(dtype='str'),
                "Grupos T3a": pd.Series(dtype='str'),
                "Creditos T4": pd.Series(dtype='str'),
                "Grupos T4": pd.Series(dtype='str'),
            })

            self.__encargoDocente  = pd.DataFrame(
            {
                "ID_PDI": pd.Series(dtype='str'),
                "ID_Asignatura": pd.Series(dtype='str'),
                "Nueva_Asignatura": pd.Series(dtype='str'),
                "Coordinación": pd.Series(dtype='str'),
                "Fecha Inicio": pd.Series(dtype='str'),
                "Fecha Fin": pd.Series(dtype='str'),
                "Creditos T": pd.Series(dtype='str'),
                "Grupos T": pd.Series(dtype='str'),
                "Creditos PA": pd.Series(dtype='str'),
                "Grupos PA": pd.Series(dtype='str'),
                "Creditos PE/PX": pd.Series(dtype='str'),
                "Grupos PE/PX": pd.Series(dtype='str'),
                "Creditos TU": pd.Series(dtype='str'),
                "Grupos TU": pd.Series(dtype='str'),
            })

    # Método que realiza un guardado de las tablas
    def save(self):
        self.__pdi.to_csv("dataBase/" + self.curso + "/pdi.csv", index=False, sep=';')
        self.__asignatura.to_csv("dataBase/" + self.curso + "/asignatura.csv", index=False, sep=';')
        self.__encargoDocente.to_csv("dataBase/" + self.curso + "/encargoDocente.csv", index=False, sep=';')

    # Método que devuelve la tabla deseada del curso
    def getTable(self, tabla):
        if tabla == "pdi":
            return self.__pdi
        elif tabla == "asignatura":
            return self.__asignatura
        elif tabla == "encargoDocente":
            return self.__encargoDocente
        else:
            return "No se ha encontrado la tabla deseada"
        
      
        

def createNewDataframe():
    master = dataframeManager()
    return master
