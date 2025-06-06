"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum_total = 0

    with open('files\input\data.csv', 'r') as file:

        for line in file:
            obs = line.split('\t')        
            if len(obs) >= 2:
                sum_total += int(obs[1])
    
    return sum_total

if __name__ == "__main__":
    print(pregunta_01())
