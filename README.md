# Game Lore RAG 🎮

Consulta documentos sobre el universo de un videojuego y encuentra los fragmentos que respaldan una respuesta. Demo educativa en Python 3.10+, sin dependencias externas.

## Ejecutar en 30 segundos

```bash
git clone https://github.com/alvaroalcalaa/game-lore-rag.git
cd game-lore-rag
python lore.py "¿Quién protege el Archivo de Cristal?"
python lore.py "¿Dónde están las piezas de la llave?"
python -m unittest -v
```

En algunos sistemas el comando es `python3`. El modo predeterminado devuelve extractos y sus fuentes: funciona sin internet, API ni modelo.

## Generación con un modelo local

Si ya tienes Ollama instalado y un modelo descargado, inicia su servicio y pasa el nombre exacto de ese modelo:

```bash
python lore.py "¿Quién protege el Archivo de Cristal?" --model NOMBRE_DE_TU_MODELO
```

El programa envía la pregunta y los fragmentos recuperados al servicio local de Ollama, en `127.0.0.1:11434`. No descarga modelos automáticamente. La generación requiere recursos de CPU/RAM o GPU según el modelo.

## Usar tus propios documentos

Añade archivos UTF-8 `.md` o `.txt` a una carpeta:

```bash
python lore.py "Tu pregunta" --docs ./mis_documentos --top-k 3
```

El corpus incluido es un universo ficticio original llamado Aurora. No contiene material de videojuegos comerciales. Usa documentos que tengas derecho a utilizar y no subas información privada.

## Cómo funciona

1. Divide los documentos en párrafos y ventanas de hasta 200 palabras con solapamiento.
2. Normaliza acentos y busca coincidencias con una puntuación BM25.
3. Recupera los mejores fragmentos y conserva nombre de archivo y número de fragmento.
4. Devuelve extractos o los pasa a un modelo local para redactar la respuesta.

Es una base RAG con recuperación léxica: no utiliza embeddings ni una base vectorial. El modo extractivo permite inspeccionar la recuperación antes de añadir generación.

## Límites conocidos

- La búsqueda no comprende sinónimos: «fundó» puede no coincidir con «fundada». Reformula o añade palabras del documento.
- Una coincidencia léxica no demuestra que el documento responda la pregunta. Sin coincidencias, el programa se abstiene; con coincidencias parciales puede recuperar contenido poco útil.
- El modelo puede inventar o citar mal. Las citas generadas no se validan automáticamente; consulta los fragmentos.
- El prompt pide ignorar instrucciones en documentos, pero no elimina el riesgo de prompt injection.
- La búsqueda recorre el corpus en cada consulta: está pensada para colecciones pequeñas.
- La integración con Ollama requiere un servicio local activo; las pruebas automatizadas no necesitan un modelo y no validan su calidad.

## Ideas para ampliarlo

Embeddings multilingües, comparación de recuperación léxica y semántica, filtros de spoilers, evaluación de citas y una interfaz de chat.
