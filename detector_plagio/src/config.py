import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CARPETA_DOCS = os.path.abspath(os.path.join(BASE_DIR, "..", "documentos"))

CARPETA_EXTERNOS = os.path.abspath(os.path.join(BASE_DIR, "..", "Documentos_Externos"))

# Crear las carpetas si no existen
os.makedirs(CARPETA_DOCS, exist_ok=True)
os.makedirs(CARPETA_EXTERNOS, exist_ok=True)

palabras_base = [
    "hola", "mundo", "tecnología", "python", "sistema", "programa", "estudiante", "documento",
    "universidad", "proyecto", "algoritmo", "hash", "similitud", "ordenamiento", "estructura",
    "datos", "texto", "comparación", "ngrama", "tabla", "función", "visualización", "código",
    "modular", "archivo", "proceso", "memoria", "optimización", "búsqueda", "eficiencia"
]
