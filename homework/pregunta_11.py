"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

    """
    file_path = 'files\input\data.csv'

    # Dictionary to store the sum of column 2 for each letter in column 4
    letter_sum = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            
            # Ensure there are enough columns (at least 2 and 4)
            if len(parts) > 3: 
                try:
                    value_col2 = int(parts[1])  # Column 2 (1-indexed)
                    letters_col4 = parts[3].split(',') # Column 4 (3-indexed)
                    
                    for letter in letters_col4:
                        if letter: # Ensure the letter is not an empty string
                            letter_sum[letter] = letter_sum.get(letter, 0) + value_col2
                except ValueError:
                    # Handle cases where the second column might not be an integer
                    pass

    # Return the dictionary with sorted keys for consistent output
    return dict(sorted(letter_sum.items()))

if __name__ == "__main__":
    print(pregunta_11())