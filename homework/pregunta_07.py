"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    file_path = "files/input/data.csv"

    # Dictionary to store lists of letters for each value in column 2
    value_to_letters = {}

    with open(file_path, 'r', encoding = "utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1:  # Ensure there's at least a first and second column
                letter = parts[0]  # Column 0
                try:
                    value = int(parts[1])  # Column 1
                    
                    if value not in value_to_letters:
                        value_to_letters[value] = []
                    value_to_letters[value].append(letter)
                except ValueError:
                    # Handle cases where the second column might not be an integer
                    pass

    # Convert the dictionary to a list of tuples and sort by the integer value
    result = sorted(value_to_letters.items())
    return result

if __name__ == "__main__":
    print(pregunta_07())
