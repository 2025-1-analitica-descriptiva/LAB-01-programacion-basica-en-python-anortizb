"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    file_path = 'files\input\data.csv'

    # Dictionary to store sets of unique letters for each value in column 2
    value_to_unique_letters = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1:  # Ensure there's at least a first and second column
                letter = parts[0]  # Column 0
                try:
                    value = int(parts[1])  # Column 1
                    
                    if value not in value_to_unique_letters:
                        value_to_unique_letters[value] = set()
                    value_to_unique_letters[value].add(letter)
                except ValueError:
                    # Handle cases where the second column might not be an integer
                    pass

    # Convert the dictionary to a list of tuples (value, sorted_list_of_unique_letters)
    result = []
    for value, letters_set in sorted(value_to_unique_letters.items()):
        result.append((value, sorted(list(letters_set))))
        
    return result

if __name__ == "__main__":
    print(pregunta_08())