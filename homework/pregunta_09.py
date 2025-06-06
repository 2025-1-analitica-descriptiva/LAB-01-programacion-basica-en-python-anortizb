"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    file_path = 'data.csv'

    # Dictionary to store the count of each key
    key_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 4:  # Ensure there's at least a fifth column
                dict_str = parts[4]
                # Split the string by commas to get individual key-value pairs
                pairs = dict_str.split(',')
                
                for pair in pairs:
                    if ':' in pair:
                        key, _ = pair.split(':') # We only need the key
                        key_counts[key] = key_counts.get(key, 0) + 1

    # Return the dictionary with sorted keys for consistent output
    return dict(sorted(key_counts.items()))

if __name__ == "__main__":
    print(pregunta_09())
