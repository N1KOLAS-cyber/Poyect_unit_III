import random
from detector_plagio.src.config import CARPETA_DOCS, palabras_base
import os

def generar_documentos(num_docs=20, palabras_por_doc=300):
    for i in range(1, num_docs + 1):
        contenido = " ".join(random.choices(palabras_base, k=palabras_por_doc))
        with open(os.path.join(CARPETA_DOCS, f"doc_{i}.txt"), "w", encoding="utf-8") as f:
            f.write(contenido)
    print(f"✅ Se generaron {num_docs} documentos con {palabras_por_doc} palabras cada uno.")
