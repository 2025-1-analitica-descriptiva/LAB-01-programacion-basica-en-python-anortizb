"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    file_path = "files/input/data.csv"

    # Dictionary to store the sum of values from column 5 for each letter in column 1
    letter_sum_col5_values = {}

    with open(file_path, 'r', encoding = "utf-8") as file:
        for line in file:
            parts = line.strip().split('\t')
            
            # Ensure there are enough columns (at least 1 and 5)
            if len(parts) > 4: 
                letter_col1 = parts[0]  # Column 1 (0-indexed)
                dict_str_col5 = parts[4] # Column 5 (4-indexed)
                
                # Split the string by commas to get individual key-value pairs
                pairs = dict_str_col5.split(',')
                
                current_sum_for_row = 0
                for pair in pairs:
                    if ':' in pair:
                        _, value_str = pair.split(':') 
                        try:
                            current_sum_for_row += int(value_str)
                        except ValueError:
                            # Handle cases where the value might not be an integer
                            pass
                
                # Add the sum of values from column 5 of the current row
                # to the corresponding letter from column 1
                letter_sum_col5_values[letter_col1] = letter_sum_col5_values.get(letter_col1, 0) + current_sum_for_row

    # Return the dictionary with sorted keys for consistent output
    return dict(sorted(letter_sum_col5_values.items()))

if __name__ == "__main__":
    print(pregunta_12())
