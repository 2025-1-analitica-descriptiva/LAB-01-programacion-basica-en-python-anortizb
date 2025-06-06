"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    file_path = 'data.csv'

    month_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 2:  # Ensure there's at least a third column
                date_str = parts[2]
                # Extract the month (MM) from the 'YYYY-MM-DD' string
                month = date_str[5:7]
                month_counts[month] = month_counts.get(month, 0) + 1

    # Convert the dictionary to a list of tuples and sort by month string
    result = sorted(month_counts.items())
    return result

if __name__ == "__main__":
    print(pregunta_04())