import os

CARPETA_DOCS = "Documentos"
CARPETA_EXTERNOS = "Documentos_Externos"

def cargar_documentos():
    documentos = {}

    # Cargar documentos generados (internos)
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

