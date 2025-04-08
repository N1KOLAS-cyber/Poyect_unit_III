import random
from detector_plagio.src.config import palabras_base

def similitud_aproximada(bf1, bf2, muestras=100):
    interseccion = 0
    union = 0
    for _ in range(muestras):
        palabra = random.choice(palabras_base)
        esta1 = palabra in bf1
        esta2 = palabra in bf2
        if esta1 or esta2:
            union += 1
        if esta1 and esta2:
            interseccion += 1
    return interseccion / union if union else 0
