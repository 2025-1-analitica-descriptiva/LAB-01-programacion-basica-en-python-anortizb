"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    file_path = 'data.csv'

    # Dictionary to store (min_value, max_value) for each key
    key_stats = {}

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) > 4:  # Ensure there's at least a fifth column
                dict_str = parts[4]
                pairs = dict_str.split(',')
                
                for pair in pairs:
                    if ':' in pair:
                        key, value_str = pair.split(':')
                        try:
                            value = int(value_str)
                            
                            if key not in key_stats:
                                key_stats[key] = [value, value]  # [min, max]
                            else:
                                current_min, current_max = key_stats[key]
                                if value < current_min:
                                    key_stats[key][0] = value
                                if value > current_max:
                                    key_stats[key][1] = value
                        except ValueError:
                            # Handle cases where the value might not be an integer
                            pass

    # Convert the dictionary to a list of tuples (key, min_value, max_value)
    # and sort alphabetically by key
    result = []
    for key, stats in sorted(key_stats.items()):
        result.append((key, stats[0], stats[1]))
        
    return result

if __name__ == "__main__":
    print(pregunta_06())
