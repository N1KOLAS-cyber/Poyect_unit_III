import os
import networkx as nx
import matplotlib.pyplot as plt


# 📁 Carpeta para guardar resultados
CARPETA_RESULTADOS = "Resultados"
os.makedirs(CARPETA_RESULTADOS, exist_ok=True)

def mostrar_grafo(similitudes, umbral=0.05):
    ruta_txt = os.path.join(CARPETA_RESULTADOS, "grafo_similitudes.txt")
    ruta_img = os.path.join(CARPETA_RESULTADOS, "grafo_similitudes.png")

    G = nx.Graph()
    conexiones_mostradas = False

    with open(ruta_txt, "w", encoding="utf-8") as f:
        f.write("🔗 Conexiones significativas (grafo textual):\n")

        for doc1, doc2, sim in similitudes:
            if sim >= umbral:
                label = f"{sim:.2%}"
                f.write(f"{doc1} --({label})--> {doc2}\n")
                G.add_edge(doc1, doc2, weight=sim, label=label)
                conexiones_mostradas = True

        if not conexiones_mostradas:
            mensaje = "❌ No hay conexiones que superen el umbral establecido.\n"
            print(mensaje)
            f.write(mensaje)
            f.write("🔧 Sugerencia: baja el umbral o mejora la calidad de los documentos.\n")
            return

    # 🎨 Dibujar grafo
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'label')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray",
            node_size=2000, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)
    plt.title("🔗 Grafo de Similitud entre Documentos")
    plt.tight_layout()
    plt.savefig(ruta_img)
    plt.close()

    print(f"📄 Grafo textual guardado en: {ruta_txt}")
    print(f"🖼️ Imagen del grafo guardada en: {ruta_img}")
