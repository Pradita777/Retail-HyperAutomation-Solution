# Solución Web de Hiperautomatización

Este proyecto es una solución web enfocada en hiperautomatización que utiliza procesamiento de lenguaje natural (LLM) y embeddings para recomendación de productos.

## Tecnologías Utilizadas
- **Backend**: FastAPI
- **Embeddings**: FAISS, SentenceTransformers
- **Modelos LLM**: Ollama con `mistral` y `all-minilm:33m`
- **Frontend**: HTML + JavaScript
- **Base de Datos**: CSV + FAISS

## Estructura del Proyecto
```
SolucionHiperautomatizacion/
│-- data/
│   └── products.csv  # Archivo de productos con las columnas: Product_ID, Product Name, Category, Description
│-- embeddings/
│   └── product_embeddings.faiss  # Índice FAISS de embeddings de productos
│-- main.py  # Servidor FastAPI para recomendación de productos
│-- create_faiss.py  # Código para generar el índice FAISS
│-- requirements.txt  # Dependencias del proyecto
│-- frontend/
│   ├── index.html  # Interfaz gráfica
│   ├── script.js  # Lógica para interactuar con la API
```

## Requisitos
1. Tener los siguientes modelos de Ollama corriendo en local:
   ```bash
   ollama list
   ```
   Salida esperada:
   ```
   NAME              ID              SIZE      MODIFIED
   all-minilm:33m    4f5da3bd944d    67 MB     7 hours ago
   mistral:latest    f974a74358d6    4.1 GB    12 days ago
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecutar el servidor FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

4. Abrir `index.html` en un navegador.

## Endpoints de la API
### `POST /recommend`
- **Descripción**: Recibe una consulta del usuario y recomienda productos basados en embeddings y un modelo LLM.
- **Body (JSON)**:
  ```json
  {
    "query": "Laptops para programar"
  }
  ```
- **Respuesta (JSON)**:
  ```json
  {
    "query": "Laptops para programar",
    "llm_response": "Based on this query, I recommend...",
    "results": [
      {
        "Product_ID": 101,
        "Product Name": "Laptop X",
        "Category": "Computers",
        "Description": "Powerful laptop for coding",
        "Similarity": 0.89
      }
    ]
  }
  ```

## Contacto
Para dudas o mejoras, abre un issue en este repositorio.

---
¡Gracias por usar esta solución! 🚀

