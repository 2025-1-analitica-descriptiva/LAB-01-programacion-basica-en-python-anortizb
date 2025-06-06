"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    file_path = "files/input/data.csv"

    sums = {}
    with open(file_path, 'r', encoding = "utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1:  # Ensure there's at least a first and second column
                first_char = parts[0][0].upper()
                try:
                    # Convert the second column to an integer and add to the sum
                    value = int(parts[1])
                    sums[first_char] = sums.get(first_char, 0) + value
                except ValueError:
                    # Handle cases where the second column might not be an integer
                    pass

    # Convert the dictionary to a list of tuples and sort alphabetically by letter
    result = sorted(sums.items())
    return result

if __name__ == "__main__":
    print(pregunta_03())
