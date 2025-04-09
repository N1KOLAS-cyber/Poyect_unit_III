# Detector de plagio para trabajos estudiantiles

La detección de plagio en trabajos estudiantiles se ha convertido en una necesidad crítica, especialmente con el fácil acceso a información en línea y la posibilidad de copiar contenido entre compañeros. Con el objetivo de fomentar la integridad académica y garantizar una evaluación justa, este proyecto presenta el desarrollo de un sistema automatizado de detección de plagio implementado en Python, diseñado para analizar similitudes entre documentos de texto plano.

Uno de los componentes fundamentales del sistema es el uso de tablas hash. Estas estructuras permiten almacenar y buscar n-gramas de forma eficiente, gracias a su capacidad de realizar operaciones de inserción y consulta en tiempo constante promedio. De esta forma, cada documento es representado como un conjunto de n-gramas únicos en su respectiva tabla hash, lo que facilita la comparación rápida entre documentos.

Para evaluar el grado de similitud entre dos documentos, se implementa la Similitud de Jaccard, una métrica que calcula el cociente entre la intersección y la unión de los conjuntos de n-gramas de dos textos. Este enfoque resulta eficaz en la detección de coincidencias parciales o patrones similares, incluso si los textos no son idénticos, ya que mide el porcentaje de contenido compartido entre los documentos.

Una vez obtenidos los valores de similitud para cada par de documentos, el sistema procede a ordenarlos utilizando el algoritmo Merge Sort, conocido por su eficiencia y estabilidad. Este algoritmo divide los datos en subconjuntos más pequeños, los ordena recursivamente y luego los combina en una lista ordenada. Su rendimiento en el peor caso O(n log⁡n) lo hace ideal para manejar listas de similitudes, especialmente cuando se trabaja con una cantidad considerable de documentos.

El sistema muestra los N documentos más similares, lo que permite identificar de manera rápida y objetiva aquellos trabajos que podrían haber sido plagiados. Esta herramienta puede ser de gran utilidad para docentes y administradores escolares, ya que automatiza un proceso que de otro modo sería manual, lento y propenso a errores.

# Instrucciones de ejecución 

Desde la raíz del proyecto, ejecuta el archivo llamado main, el cual tiene la función de :

* Generar 50 documentos de prueba con 300 palabras cada uno.

* Procesará todos los documentos, limpiando el texto y generando n-gramas de tamaño 3.

* Insertará los n-gramas en filtros de Bloom.

* Comparará todos los pares de documentos calculando la similitud.

* Ordenará los pares por similitud usando Merge Sort.

* Imprimirá en consola los 10 pares de documentos más similares.

* Mostrará un grafo visual, donde los nodos son documentos y las aristas representan alto nivel de similitud.

Los parametros que se pueden modificar igualmente se encuentran en el archivo raíz main, donde se pueden modificar: 

* num_docs: número de documentos a generar.

* palabras_por_doc: cantidad de palabras por documento.

* ngram_size: tamaño de los n-gramas.

* top_n: cantidad de resultados más similares a mostrar.

Igualmente se pueden cargar documentos a comparar en la llamada carpeta ** Documentos_Externos ** 
donde se encuentran dos documentos que no son generados por el programa ni por el programa raiz main 
que son comparados para detectar su similitud. 

# Ejemplos de uso 

La integridad académica es fundamental en las instituciones educativas, y la detección de plagio juega un papel crucial en su mantenimiento. Herramientas especializadas son ampliamente utilizadas por universidades para identificar similitudes en trabajos estudiantiles, asegurando la originalidad y el respeto por los derechos de autor. Estas tecnologías permiten a los docentes detectar coincidencias exactas en palabras clave, frases y oraciones, lo cual facilita la identificación de posibles casos de plagio y refuerza el compromiso con la honestidad académica.

Sin embargo, algunos sistemas automatizados pueden generar falsos positivos, especialmente cuando analizan textos escritos por estudiantes cuya lengua materna no es el idioma de instrucción. Por esta razón, se recomienda que los docentes complementen el uso de estas herramientas con una revisión personal y un juicio académico informado.

Más allá de su uso en instituciones educativas, este tipo de tecnología encuentra también un espacio relevante en otros entornos donde la originalidad y la propiedad intelectual son fundamentales. En el ámbito periodístico, por ejemplo, es útil para verificar que los artículos no sean réplicas de publicaciones anteriores, protegiendo la credibilidad de los medios. En el sector corporativo, puede emplearse para revisar documentos internos y prevenir el uso no autorizado de contenido externo, especialmente en informes o materiales legales. En el mundo editorial y científico, sirve como herramienta previa a la publicación para evitar conflictos de derechos de autor y asegurar la autenticidad del contenido.

El desarrollo de herramientas propias, como el sistema de detección de plagio que emplea estructuras eficientes como los filtros de Bloom y algoritmos de comparación mediante n-gramas, representa una alternativa accesible y personalizable para contextos educativos diversos. Estas soluciones pueden integrarse fácilmente en entornos académicos para apoyar tanto la evaluación del contenido como el proceso formativo de los estudiantes. 
