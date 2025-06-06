"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    file_path = 'files\input\data.csv'

    counts = {}
    with open(file_path, 'r') as file:
        for line in file:

            parts = line.strip().split('\t')
            if parts:
                first_char = parts[0][0].upper()  # Get the first character and convert to uppercase
                counts[first_char] = counts.get(first_char, 0) + 1

    # Convert the dictionary to a list of tuples and sort alphabetically by letter
    result = sorted(counts.items())
    return result

if __name__ == "__main__":
    print(pregunta_02())
