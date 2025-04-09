import os
from src.config import CARPETA_DOCS, CARPETA_EXTERNOS  # Importar CARPETA_DOCS desde config.py
from collections import defaultdict
import hashlib

def cargar_documentos():
    documentos = {}

    # Cargar documentos generados (internos) usando la ruta definida en config.py
    for archivo in os.listdir(CARPETA_DOCS):
        if archivo.endswith(".txt"):
            ruta = os.path.join(CARPETA_DOCS, archivo)
            with open(ruta, "r", encoding="utf-8") as f:
                documentos[archivo] = f.read()

    # Cargar documentos externos
    if os.path.exists(CARPETA_EXTERNOS):
        for archivo in os.listdir(CARPETA_EXTERNOS):
            if archivo.endswith(".txt"):
                ruta = os.path.join(CARPETA_EXTERNOS, archivo)
                with open(ruta, "r", encoding="utf-8") as f:
                    documentos[f"(externo) {archivo}"] = f.read()

    return documentos

import re

def limpiar_y_tokenizar(texto, n=3):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    palabras = texto.split()
    return [' '.join(palabras[i:i+n]) for i in range(len(palabras)-n+1)]

# Función para generar la tabla hash de n-gramas
def generar_hash_ngramas(documentos, n=3):
    tabla_hash_ngramas = defaultdict(set)

    # Iterar sobre cada documento
    for nombre_archivo, contenido in documentos.items():
        # Limpiar y tokenizar el texto
        ngramas = limpiar_y_tokenizar(contenido, n)

        # Generar n-gramas y almacenarlos en la tabla hash
        for ngrama in ngramas:
            # Crear un hash único para el n-grama
            hash_ngram = hashlib.md5(ngrama.encode('utf-8')).hexdigest()
            # Agregar el n-grama al conjunto correspondiente en la tabla hash
            tabla_hash_ngramas[hash_ngram].add((nombre_archivo, ngrama))

    return tabla_hash_ngramas