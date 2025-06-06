"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    file_path = "files/input/data.csv"

    # Dictionary to store (max_value, min_value) for each letter
    letter_stats = {}

    with open(file_path, 'r', encoding = "utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 1:
                letter = parts[0][0].upper()
                try:
                    value = int(parts[1])

                    if letter not in letter_stats:
                        letter_stats[letter] = [value, value]  # [max, min]
                    else:
                        current_max, current_min = letter_stats[letter]
                        if value > current_max:
                            letter_stats[letter][0] = value
                        if value < current_min:
                            letter_stats[letter][1] = value
                except ValueError:
                    # Handle cases where the second column might not be an integer
                    pass

    # Convert the dictionary to a list of tuples (letter, max_value, min_value)
    # and sort alphabetically by letter
    result = []
    for letter, stats in sorted(letter_stats.items()):
        result.append((letter, stats[0], stats[1]))
        
    return result

if __name__ == "__main__":
    print(pregunta_05())
