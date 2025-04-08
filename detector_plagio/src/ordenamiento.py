def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izq, der):
    resultado = []
    while izq and der:
        if izq[0][2] > der[0][2]:  # Ordena por el valor de similitud
            resultado.append(izq.pop(0))
        else:
            resultado.append(der.pop(0))
    resultado.extend(izq)
    resultado.extend(der)
    return resultado
