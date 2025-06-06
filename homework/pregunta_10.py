"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    file_path = "files/input/data.csv"

    result = []
    with open(file_path, 'r', encoding = "utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            
            # Ensure there are enough columns
            if len(parts) > 4: 
                letter = parts[0]  # Column 1 (0-indexed)
                
                # Count elements in column 4 (3-indexed)
                # Split by comma and count the resulting elements. Handle empty string case.
                col4_elements = parts[3].split(',')
                count_col4 = len(col4_elements) if parts[3] else 0

                # Count elements in column 5 (4-indexed)
                # Split by comma and count the resulting elements. Handle empty string case.
                col5_elements = parts[4].split(',')
                count_col5 = len(col5_elements) if parts[4] else 0
                
                result.append((letter, count_col4, count_col5))
                
    return result

if __name__ == "__main__":
    print(pregunta_10())