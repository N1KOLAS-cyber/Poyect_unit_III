from src.generador import generar_documentos
from src.procesamiento import cargar_documentos, limpiar_y_tokenizar, generar_hash_ngramas
from src.bloomfilter import crear_tabla_bloom
from src.similitud import similitud_aproximada
from src.ordenamiento import merge_sort
from src.visualizacion import mostrar_grafo
from itertools import combinations

def comparar_documentos(ngram_size=3, top_n=10):
    documentos = cargar_documentos()
    tablas_bloom = {}

    # Generar la tabla hash de n-gramas y mostrarla
    print("TABLA HASH DE N-GRAMAS")
    tabla_hash = generar_hash_ngramas(documentos, n=ngram_size)
    for hash_ngram, archivos in tabla_hash.items():
        print(f"{hash_ngram}: {archivos}")
    
    # Crear las tablas de Bloom para cada documento
    for nombre, contenido in documentos.items():
        ngramas = limpiar_y_tokenizar(contenido, ngram_size)
        tablas_bloom[nombre] = crear_tabla_bloom(ngramas)

    # Calcular similitudes
    similitudes = []
    for doc1, doc2 in combinations(tablas_bloom.keys(), 2):
        sim = similitud_aproximada(tablas_bloom[doc1], tablas_bloom[doc2])
        similitudes.append((doc1, doc2, sim))

    # Ordenar similitudes
    similitudes_ordenadas = merge_sort(similitudes)

    # Mostrar los documentos más similares
    print(f"\n🔝 Top {top_n} documentos más similares:")
    for doc1, doc2, sim in similitudes_ordenadas[:top_n]:
        print(f"{doc1} <-> {doc2} | Similitud: {sim:.2%}")

    # Visualizar el grafo de similitudes
    mostrar_grafo(similitudes_ordenadas[:10])

if __name__ == "__main__":
    generar_documentos(num_docs=50, palabras_por_doc=300)
    comparar_documentos(ngram_size=3, top_n=10)
